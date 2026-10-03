"""Configuración de la base de datos con SQLAlchemy."""

from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

from app.config import settings


engine = create_engine(
    settings.database_url,
    connect_args={"check_same_thread": False} if "sqlite" in settings.database_url else {},
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


class Base(DeclarativeBase):
    """Clase base para todos los modelos ORM."""

    pass


def get_db():
    """Dependencia que provee una sesión de base de datos por request."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()