"""Esquemas Pydantic para validación de datos de Task."""

from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field


class TaskBase(BaseModel):
    """Campos comunes para tareas."""

    title: str = Field(..., min_length=1, max_length=100, description="Título de la tarea")
    description: str | None = Field(None, max_length=500, description="Descripción opcional")
    completed: bool = Field(default=False, description="Estado de la tarea")


class TaskCreate(TaskBase):
    """Esquema para crear una tarea."""

    pass


class TaskUpdate(BaseModel):
    """Esquema para actualizar una tarea (todos los campos opcionales)."""

    title: str | None = Field(None, min_length=1, max_length=100)
    description: str | None = Field(None, max_length=500)
    completed: bool | None = None


class TaskResponse(TaskBase):
    """Esquema de respuesta para una tarea."""

    id: int
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)