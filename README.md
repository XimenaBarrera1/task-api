# Task API 🚀

API REST para gestión de tareas desarrollada con **FastAPI**, **SQLAlchemy** y **SQLite**.

## 🛠️ Tecnologías

- **Python 3.13**
- **FastAPI** — Framework web moderno y de alto rendimiento
- **SQLAlchemy 2.0** — ORM con sintaxis moderna
- **Pydantic** — Validación de datos
- **SQLite** — Base de datos ligera
- **pytest** — Testing

## ✨ Características

- CRUD completo de tareas (Crear, Leer, Actualizar, Eliminar)
- Validación automática de datos con Pydantic
- Documentación interactiva con Swagger UI
- Arquitectura por capas (modelos, esquemas, servicios, routers)
- Configuración mediante variables de entorno
- Tests automatizados con pytest

## 📁 Estructura del proyecto

```
task-api/
├── app/
│   ├── __init__.py
│   ├── main.py              # Punto de entrada
│   ├── config.py            # Configuración
│   ├── database.py          # Conexión a BD
│   ├── models/              # Modelos ORM
│   │   ├── __init__.py
│   │   └── task.py
│   ├── schemas/             # Esquemas Pydantic
│   │   ├── __init__.py
│   │   └── task.py
│   ├── routers/             # Endpoints HTTP
│   │   ├── __init__.py
│   │   └── tasks.py
│   └── services/            # Lógica de negocio
│       ├── __init__.py
│       └── task_service.py
├── tests/
│   ├── __init__.py
│   ├── conftest.py
│   └── test_tasks.py
├── .env.example
├── .gitignore
├── pyproject.toml
├── requirements.txt
└── README.md
```

## 🚀 Instalación y uso

### 1. Clonar el repositorio

```bash
git clone https://github.com/XimenaBarrera1/task-api.git
cd task-api
```

### 2. Crear y activar entorno virtual

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4. Configurar variables de entorno

```bash
cp .env.example .env
```

### 5. Ejecutar el servidor

```bash
uvicorn app.main:app --reload
```

Abre tu navegador en: **http://127.0.0.1:8000/docs**

## 🧪 Ejecutar tests

```bash
pytest -v
```

## 📌 Endpoints

| Método | Ruta | Descripción |
|--------|------|-------------|
| GET | `/` | Información de la API |
| GET | `/tasks/` | Listar todas las tareas |
| POST | `/tasks/` | Crear una nueva tarea |
| GET | `/tasks/{id}` | Obtener una tarea por ID |
| PUT | `/tasks/{id}` | Actualizar una tarea |
| DELETE | `/tasks/{id}` | Eliminar una tarea |

## 📋 Ejemplo de uso

### Crear una tarea

```bash
curl -X POST "http://127.0.0.1:8000/tasks/" \
  -H "Content-Type: application/json" \
  -d '{"title": "Mi primera tarea", "description": "Aprender FastAPI"}'
```

### Listar tareas

```bash
curl "http://127.0.0.1:8000/tasks/"
```

## 👤 Autor
 
Ximena Barrera C


## 📄 Licencia

Este proyecto está bajo la Licencia MIT.