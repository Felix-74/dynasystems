# Notes API
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)![Django](https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white)
![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)![Django](https://img.shields.io/badge/drf-%23092E20.svg?style=for-the-badge&labelColor=blue&logo=django&logoColor=white)
### Описание
Notes REST API - это простой API для управления заметками. API позволяет создавать, просматривать, обновлять и удалять заметки.
### Требования к системе 
Python 3.8+
Django 4.2
Django REST Framework
drf-yasg (для документации Swagger и ReDoc)

### Установка
Клонировать репозиторий и перейти в него в командной строке:
```
git clone git@github.com:Felix-74/dynasystems.git
``` 
Перейти в папку с приложением:
```
cd Notes_№3
cd notesRest
``` 
Установить и активировать виртуальное окружение:
``` 
python -m venv env
source env/bin/activate  # На Windows используйте `env\Scripts\activate`
```
Установить зависимости из файла requirements.txt:
```
python3 -m pip install --upgrade pip
pip install -r requirements.txt
``` 
Выполнить миграции:
```
python manage.py migrate
```
Создайте суперпользователя:
```
python manage.py createsuperuser
```

Запустить проект:
```
python manage.py runserver 5577
```

### Конечные точки API
Список всех заметок
- URL: /api/notes/
- Метод: GET
-Ответ:
```
[
    { "id": 1, "note": "Первая заметка", "description": "Описание первой заметки" },
    { "id": 2, "note": "Вторая заметка", "description": "Описание второй заметки" }
]
```
Получение заметки по ID
- URL: /api/notes/<item_id>/
- Метод: GET
-Ответ:
```
{
    "id": 1,
    "note": "Первая заметка",
    "description": "Описание первой заметки"
}
```
Создание новой заметки
- URL: /api/notes/
- Метод: POST
-Тело запроса:
```
{
    "note": "Новая заметка",
    "description": "Описание новой заметки"
}
```
Ответ:
```
{
    "id": 3
}
```
Удаление заметки
- URL: /api/tasks/<item_id>/
- Метод: DELETE
- Ответ: Пустое тело ответа.

Обновление заметки
- URL: /api/tasks/<item_id>/
- Метод: PUT
-Тело запроса:
```
{
    "note": "Обновленная заметка",
    "description": "Обновленное описание заметки"
}
```
Ответ:
```
{
    "id": 1,
    "note": "Обновленная заметка",
    "description": "Обновленное описание заметки"
}
```
Документация проекта расположена по [адресу:](http://127.0.0.1:8000/swagger)

```
http://127.0.0.1:8000/swagger/
```


