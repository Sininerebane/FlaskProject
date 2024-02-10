Сервис для работы с Календарем.

Требования:

— API интерфейс CRUD — Добавление / Список / Чтение / Обновление / Удаление
— модель данных "Событие": ID, Дата, Заголовок, Текст
— локальное хранилище данных
— максимальная длина заголовка — 30 символов
— максимальная длина поля Текст — 200 символов
— нельзя добавить больше одного события в день
— API интерфейс: /api/v1/
— формат данных: "ГГГГ-ММ-ДД|заголовок|текст" 

### добавление нового события

curl http://127.0.0.1:5000/api/v1/event/ -X POST -d "2024-02-09|title1|text1"
New event created: title1. Date: 2024-02-09. id: 20240209

curl http://127.0.0.1:5000/api/v1/event/ -X POST -d "2024-02-10|title2|text2"
New event created: title2. Date: 2024-02-10. id: 20240210

curl http://127.0.0.1:5000/api/v1/event/ -X POST -d "2024-02-09|title3|text3"
Failed: You can add only one event for one day

curl http://127.0.0.1:5000/api/v1/event/ -X POST -d "2024-02-09|title2somethingggggggggggggggggggg|text2"
Failed: Title length > max: 30

curl http://127.0.0.1:5000/api/v1/event/ -X POST -d "2024-02-09|title4|textsomthinggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggg"
Failed: Text length > max: 200

### получение всего списка событий

curl http://127.0.0.1:5000/api/v1/event/
2024-02-09|title1|text1
2024-02-10|title2|text2

### получение события по идентификатору / ID == 20240209

curl http://127.0.0.1:5000/api/v1/event/20240209/
2024-02-09|title1|text1

### обновление текста события по идентификатору / ID == 20240209 /  новый текст == "текст1updated"

curl http://127.0.0.1:5000/api/v1/event/20200530/ -X PUT -d "2024-02-09|title1|text1updated "
Event id: 20240209 updated

### получение обновленного события по идентификатору / ID == 20240209

curl http://127.0.0.1:5000/api/v1/event/20200530/
2024-02-09|title1|text1updated

### получение всего списка событий

curl http://127.0.0.1:5000/api/v1/event/

2024-02-09|title1|text1updated
2024-02-10|title2|text2

### удаление события по идентификатору / ID == 20240209
 
curl http://127.0.0.1:5000/api/v1/event/20200530/  -X DELETE
Event id:20240209 deleted

### получение всего списка событий

curl http://127.0.0.1:5000/api/v1/event/
2024-02-10|title2|text2
