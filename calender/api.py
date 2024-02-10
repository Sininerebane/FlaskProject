from flask import Flask, request, render_template
from datetime import datetime

import model
import logic

app = Flask(__name__)

API_ROOT = '/api/calender/v1'
EVENT_API_ROOT = API_ROOT + '/event'

my_storage = logic.Eventlogic()


class ApiException(Exception):
    pass


def from_raw_to_event(raw_event: str) -> model.Event:
    try:
        event_list_data = raw_event.split('|')
        event_id = event_list_data[0].replace('-', '')
        day = datetime.strptime(event_list_data[0], '%Y-%m-%d')
        title = event_list_data[1]
        text = event_list_data[2]
        event = model.Event(event_id, day, title, text)
        return event
    except Exception as ex:
        raise ApiException("Incorrect Format")


def to_raw(event: model.Event) -> str:
    return f'{event.day.strftime("%Y-%m-%d")}|{event.title}|{event.text}'


@app.route(API_ROOT + '/')
def main():
    return render_template('main.html')


@app.route(API_ROOT + '/about/')
def about():
    return render_template('about.html')


@app.route(EVENT_API_ROOT + '/', methods=['POST'])
def create():
    try:
        data = request.get_data().decode('utf-8')
        event = from_raw_to_event(data)
        my_storage.create(event)
        return f'New event created: {event.title}. Date: {event.day.strftime("%Y-%m-%d")}. id: {event.event_id}'
    except Exception as ex:
        return f"failed to Create with: {ex}", 404


@app.route(EVENT_API_ROOT + '/', methods=['GET'])
def list():
    try:
        raw = ''
        for elem in my_storage.list():
            raw += to_raw(elem) + '\n'
        return raw
    except Exception as ex:
        return f"failed to LIST with: {ex}", 404


@app.route(EVENT_API_ROOT + '/<event_id>/', methods=['GET'])
def read(event_id: str):
    try:
        result = my_storage.read(event_id)
        return to_raw(result)
    except Exception as ex:
        return f"failed to READ with: {ex}", 404


@app.route(EVENT_API_ROOT + '/<event_id>/', methods=['PUT'])
def update(event_id: str):
    try:
        data = request.get_data().decode('utf-8')
        event = from_raw_to_event(data)
        my_storage.update(event_id, event)
        return f'Event id: {event_id} updated'
    except Exception as ex:
        return f"failed to UPDATE with: {ex}", 404


@app.route(EVENT_API_ROOT + '/<event_id>/', methods=["DELETE"])
def delete(event_id: str):
    try:
        my_storage.delete(event_id)
        return f'Event id:{event_id} deleted'
    except Exception as ex:
        return f"failed to DELETE with: {ex}", 404


if __name__ == '__main__':
    app.run(debug=True)
