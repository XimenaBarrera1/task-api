"""Punto de entrada de la aplicación FastAPI."""

from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.config import settings
from app.database import Base, engine
from app.routers import tasks


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Crea las tablas de la BD al iniciar la aplicación."""
    Base.metadata.create_all(bind=engine)
    yield


app = FastAPI(
    title=settings.app_name,
    description="API REST para gestión de tareas",
    version="1.0.0",
    lifespan=lifespan,
)

app.include_router(tasks.router)


@app.get("/", tags=["Root"])
def root():
    """Endpoint raíz con información básica de la API."""
    return {
        "app": settings.app_name,
        "version": "1.0.0",
        "docs": "/docs",
        "redoc": "/redoc",
    }