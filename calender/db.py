import storage
import model


class DBException(Exception):
    pass


class DB:
    def __init__(self):
        self.storage = storage.LocalStorage()

    def create(self, event: model.Event):
        try:
            return self.storage.create(event)
        except Exception as ex:
            raise DBException(f"failed CREATE operation with: {ex}")

    def list(self):
        try:
            return self.storage.list()
        except Exception as ex:
            raise DBException(f"failed LIST operation with: {ex}")

    def read(self, event_id: str):
        try:
            return self.storage.read(event_id)
        except Exception as ex:
            raise DBException(f"failed READ operation with: {ex}")

    def update(self, event_id: str, event: model.Event):
        try:
            self.storage.update(event_id, event)
        except Exception as ex:
            raise DBException(f"failed UPDATE operation with: {ex}")

    def delete(self, event_id: str):
        try:
            self.storage.delete(event_id)
        except Exception as ex:
            raise DBException(f"failed DELETE operation with: {ex}")
