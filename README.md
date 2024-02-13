
# Сервис для работы с Календарем.
## краткая инструкция по использованию сервиса для работы с календарем. 
в инструкции указаны примеры запросов, HTTP метод и соответствующие URL для осуществления операций

Для запуска сервиса надо открыть папку проета в терминале  (cmd) и запустить следующий команду: flask --app ./calender/server.py run
Как толлько сервис запущен запустите следующие команды:
### добавление нового события
curl http://127.0.0.1:5000/api/v1/event/ -X POST -d "date|title1|text1"
### получение всего списка событий
curl http://127.0.0.1:5000/api/v1/event/
### получение события по идентификатору / ID 
curl http://127.0.0.1:5000/api/v1/event/put id here/
### обновление текста события по идентификатору / ID  /  новый текст 
curl http://127.0.0.1:5000/api/v1/event/ID/ -X PUT -d "date|title1|Put updated text here "
### удаление события по идентификатору / ID
curl http://127.0.0.1:5000/api/v1/event/put id here/  -X DELETE


Следующие требования были выполнениы при создании календаря:
* API интерфейс CRUD — Добавление / Список / Чтение / Обновление / Удаление
* модель данных "Событие": ID, Дата, Заголовок, Текст
* локальное хранилище данных
* максимальная длина заголовка — 30 символов
* максимальная длина поля Текст — 200 символов
* нельзя добавить больше одного события в день
* API интерфейс: /api/v1/
* формат данных: "ГГГГ-ММ-ДД|заголовок|текст" 

