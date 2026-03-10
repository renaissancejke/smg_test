# URL Shortener

Микросервис для сокращения ссылок на FastAPI + PostgreSQL.

## Стек

| Слой | Технология |
|------|-----------|
| Framework | FastAPI |
| База данных | PostgreSQL 16 |
| ORM | SQLAlchemy 2 |
| Миграции | Alembic |
| Контейнеризация | Docker + docker-compose |
| Тесты | pytest + httpx |

---

## Быстрый старт (Docker Compose)

```bash
# 1. Клонировать репозиторий
git clone <repo-url>
cd url-shortener

# 2. Создать .env из примера
cp .env.example .env

# 3. Запустить
docker compose up --build
```

API будет доступен по адресу: **http://localhost:8000**

Документация (Swagger): **http://localhost:8000/docs**

---

## Запуск локально (без Docker)

```bash
# 1. Создать виртуальное окружение
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# 2. Установить зависимости
pip install -r requirements.txt

# 3. Настроить переменные окружения
cp .env.example .env
# Отредактировать .env: указать реальный DATABASE_URL

# 4. Применить миграции
alembic upgrade head

# 5. Запустить сервер
uvicorn app.main:app --reload
```

---

## API

### `POST /shorten` — сократить ссылку

**Request:**
```json
{ "url": "https://www.example.com/some/very/long/path?query=1" }
```

**Response `201`:**
```json
{
  "short_id": "aB3xY9z",
  "short_url": "http://localhost:8000/aB3xY9z",
  "original_url": "https://www.example.com/some/very/long/path?query=1"
}
```

---

### `GET /{short_id}` — редирект

Перенаправляет на оригинальный URL (`302 Found`) и увеличивает счётчик переходов.

---

### `GET /stats/{short_id}` — статистика

**Response `200`:**
```json
{
  "short_id": "aB3xY9z",
  "original_url": "https://www.example.com/some/very/long/path?query=1",
  "clicks": 42,
  "created_at": "2024-05-01T12:00:00"
}
```

---

## Тесты

```bash
# Установить зависимости (если ещё не установлены)
pip install -r requirements.txt

# Запустить тесты
pytest tests/ -v
```

Тесты используют SQLite in-memory — PostgreSQL для запуска не нужен.

---

## Структура проекта

```
url-shortener/
├── app/
│   ├── main.py          # FastAPI роутеры
│   ├── models.py        # SQLAlchemy модель Link
│   ├── schemas.py       # Pydantic схемы
│   ├── crud.py          # Работа с БД
│   ├── shortener.py     # Генерация short_id
│   ├── database.py      # Подключение к БД
│   └── config.py        # Настройки (pydantic-settings)
├── alembic/
│   └── versions/
│       └── 0001_create_links.py
├── tests/
│   └── test_main.py
├── Dockerfile
├── docker-compose.yml
├── alembic.ini
├── requirements.txt
└── .env.example
```
