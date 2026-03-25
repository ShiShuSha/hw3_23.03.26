## Домашнее задание 4 к теме 4

В предыдущем домашнем задании к теме «Работа с базами данных: FastAPI, SQLAlchemy, Alembic» вы разработали модель данных для хранения данных из CSV-файла.

## Запуск

```
pip install fastapi uvicorn sqlalchemy
uvicorn main:app --reload
```

## Описание задачи

Дан CSV-файл `students.csv`, содержащий данные о студентах:

* Фамилия
* Имя
* Факультет
* Курс (предмет)
* Оценка

Необходимо:

1. Разработать модель данных
2. Реализовать её с помощью SQLAlchemy
3. Подключить Alembic
4. Создать и применить миграции

---

## Архитектура базы данных

### 1. Students

* id (PK)
* first_name
* last_name
* faculty

### 2. Courses

* id (PK)
* name (уникальное)

### 3. Grades

* id (PK)
* student_id (FK → Students)
* course_id (FK → Courses)
* grade

---

## 📁 Структура проекта

```
project/
│
├── models.py          # SQLAlchemy модели
├── database.py        # Подключение к БД
├── students.csv       # Исходные данные
│
├── alembic/           # Миграции
├── alembic.ini
│
└── README.md
```

---

## Установка и запуск

### 1. Клонировать репозиторий

```
git clone <ссылка на репозиторий>
cd project
```

### 2. Установить зависимости

```
pip install sqlalchemy alembic
```

---

## Работа с миграциями

### Инициализация Alembic (если не сделано)

```
alembic init alembic
```

### Создание миграции

```
alembic revision --autogenerate -m "create tables"
```

### Применение миграций

```
alembic upgrade head
```

Данные из CSV можно дополнительно загрузить в базу данных с помощью отдельного скрипта (опционально).
