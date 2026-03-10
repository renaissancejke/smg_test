# URL Shortener

Микросервис для сокращения ссылок на FastAPI + PostgreSQL.

## Запуск

Нужен только Docker.

```bash
git clone <repo-url>
cd url-shortener

cp .env.example .env

docker compose up --build
```

Готово. Миграции применяются автоматически.

- Swagger UI: **http://localhost:8000/docs**

## API

| Метод | Эндпоинт | Описание |
|-------|----------|----------|
| `POST` | `/shorten` | Сократить ссылку |
| `GET` | `/{short_id}` | Редирект на оригинальный URL |
| `GET` | `/stats/{short_id}` | Количество переходов |

Пример:
```bash
curl -X POST http://localhost:8000/shorten \
  -H "Content-Type: application/json" \
  -d '{"url": "https://example.com/very/long/url"}'

# {"short_id": "aB3xY9z", "short_url": "http://localhost:8000/aB3xY9z"}
```

> `GET /{short_id}` возвращает 302 редирект — проверяй в браузере, не через Swagger.

## Тесты

Требуется Python 3.12.

```bash
python -m venv .venv
.venv\Scripts\activate      # Windows
# source .venv/bin/activate # Mac/Linux

pip install -r requirements.txt
pytest tests/ -v
```
