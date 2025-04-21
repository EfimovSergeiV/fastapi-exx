from fastapi import FastAPI
from models import Base
from database import engine
from routes import items, echo



app = FastAPI(
    title="Example API",
    description="Простой пример на FastAPI",
    version="1.0.0"
)

Base.metadata.create_all(bind=engine)



app.include_router(items.router)
app.include_router(echo.router)