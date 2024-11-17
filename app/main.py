from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import course_routes, websocket_routes, webhook_routes
import uvicorn

app = FastAPI()

# Разрешаем CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Разрешить все домены (можно ограничить в продакшн)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Подключение маршрутов
app.include_router(course_routes.router)
app.include_router(websocket_routes.router)
app.include_router(webhook_routes.router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
