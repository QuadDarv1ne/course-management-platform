# 🧑‍🏫 Course Management Platform

**Платформа управления онлайн-курсами** с использованием современных технологий API взаимодействий:

- **REST API** для CRUD-операций.
- **gRPC** для межсервисного взаимодействия.
- **WebSocket** для уведомлений в реальном времени.
- **Webhook** для интеграции с внешними системами.

---

## 📋 Содержание

- [Описание](#описание)
- [Функционал](#функционал)
- [Технологии](#технологии)
- [Установка](#установка)
- [Использование](#использование)
- [Примеры API](#примеры-api)
- [Контакты](#контакты)

---

## 📝 Описание

Этот проект представляет собой модульную систему для управления курсами. Он демонстрирует использование различных способов взаимодействия API, что позволяет интегрировать платформу с другими сервисами, обеспечивать высокую производительность и поддерживать реальное время работы.

---

## ✨ Функционал

1. **REST API**:
   - Управление курсами (CRUD-операции).
   - Авторизация и аутентификация.

2. **gRPC**:
   - Взаимодействие с микросервисом аналитики.

3. **WebSocket**:
   - Уведомления о новых курсах и активностях пользователей.

4. **Webhook**:
   - Обработка уведомлений от платёжных систем.

---

## 🛠️ Технологии

- Backend:
  - **FastAPI**
  - **gRPC**
  - **WebSocket**
- Брокеры сообщений:
  - **Kafka**
  - **RabbitMQ**
- СУБД:
  - **PostgreSQL**
- Инфраструктура:
  - **Docker**
  - **NGINX** (для прокси и балансировки).
  
---

## 🚀 Установка

### 1. Клонируйте репозиторий
```bash
git clone https://github.com/username/course-management-platform.git
cd course-management-platform
```

### 2. Установите зависимости

**Создайте и активируйте виртуальное окружение:**

```bash
python -m venv venv
source venv/bin/activate  # Linux/MacOS
venv\Scripts\activate  # Windows
```

**Установите зависимости:**

```bash
pip install -r requirements.txt
```

### 3. Запустите сервисы через Docker

Убедитесь, что Docker установлен.

**Запустите контейнеры:**

```
docker-compose up -d
```

### 4. Запустите приложение

```bash
uvicorn main:app --reload
```

**Приложение будет доступно по адресу:** `http://localhost:8000`

### 🛡️ Использование

1. Документация API

**Откройте в браузере:**

1. `Swagger UI:` http://localhost:8000/docs
2. `ReDoc:` http://localhost:8000/redoc

2. Тестирование WebSocket

`Подключитесь к WebSocket`: ws://localhost:8000/ws/

### 📚 Примеры API

1. REST API

**Создание курса:**

```bash
curl -X POST http://localhost:8000/courses/ -H "Content-Type: application/json" -d '{"title": "Python Basics", "description": "Learn Python from scratch"}'
```

**Получение списка курсов:**

```bash
curl http://localhost:8000/courses/
```

2. gRPC

Используйте клиента, чтобы отправить данные на микросервис аналитики.

3. Webhook

**Симулируйте запрос от внешней системы:**

```bash
curl -X POST http://localhost:8000/webhook/payment/ -H "Content-Type: application/json" -d '{"payment
```

### 📈 Структура репозитория

```
course-management-platform/
│
├── app/
│   ├── __init__.py           # Инициализация приложения
│   ├── main.py               # Основное приложение FastAPI
│   ├── grpc/                     # gRPC-сервис и клиент
│   │   ├── server.py             # gRPC сервер
│   │   ├── client.py             # gRPC клиент
│   │   └── course.proto          # Определение gRPC сервиса
│   │
│   ├── routes/                   # Маршруты (REST API, Webhook, WebSocket)
│   │   ├── course_routes.py      # Маршруты для работы с курсами (REST)
│   │   ├── websocket_routes.py   # Маршруты для WebSocket
│   │   └── webhook_routes.py     # Маршруты для Webhook
│   │
│   ├── models/                   # Модели базы данных
│   │   └── course_model.py       # Модель курса для работы с базой данных
│   │
│   ├── websocket/                # Логика для WebSocket
│   └── config.py                 # Конфигурация приложения            
│
├── docker-compose.yml         # Конфигурация Docker
├── requirements.txt           # Зависимости проекта
├── README.md                  # Документация
└── .env                       # Переменные окружения
```

### 🤝 Контакты

**Автор:** Дуплей Максим Игоревич

**Email:** maksimqwe42@mail.ru

**Дата:** 16.11.2024

- ✨ Этот проект создан для демонстрации взаимодействий API и обучения разработке веб-сервисов.
