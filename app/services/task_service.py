"""Lógica de negocio para las tareas."""

from sqlalchemy.orm import Session

from app.models.task import Task
from app.schemas.task import TaskCreate, TaskUpdate


def get_all_tasks(db: Session, skip: int = 0, limit: int = 100) -> list[Task]:
    """Obtiene todas las tareas con paginación."""
    return db.query(Task).offset(skip).limit(limit).all()


def get_task_by_id(db: Session, task_id: int) -> Task | None:
    """Obtiene una tarea por su ID."""
    return db.query(Task).filter(Task.id == task_id).first()


def create_task(db: Session, task_data: TaskCreate) -> Task:
    """Crea una nueva tarea."""
    new_task = Task(**task_data.model_dump())
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task


def update_task(db: Session, task_id: int, task_data: TaskUpdate) -> Task | None:
    """Actualiza una tarea existente."""
    task = get_task_by_id(db, task_id)
    if task is None:
        return None

    update_data = task_data.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(task, field, value)

    db.commit()
    db.refresh(task)
    return task


def delete_task(db: Session, task_id: int) -> bool:
    """Elimina una tarea. Devuelve True si existía, False si no."""
    task = get_task_by_id(db, task_id)
    if task is None:
        return False

    db.delete(task)
    db.commit()
    return True