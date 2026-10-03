"""Tests para los endpoints de tareas."""


def test_read_root(client):
    """El endpoint raíz debe responder con la info de la API."""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["app"] == "Task API"


def test_create_task(client):
    """Debe crear una tarea correctamente."""
    response = client.post(
        "/tasks/",
        json={"title": "Aprender FastAPI", "description": "Completar el proyecto"},
    )
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == "Aprender FastAPI"
    assert data["completed"] is False
    assert "id" in data


def test_list_tasks(client):
    """Debe listar las tareas existentes."""
    client.post("/tasks/", json={"title": "Tarea 1"})
    client.post("/tasks/", json={"title": "Tarea 2"})

    response = client.get("/tasks/")
    assert response.status_code == 200
    assert len(response.json()) >= 2


def test_get_task_by_id(client):
    """Debe obtener una tarea por su ID."""
    post = client.post("/tasks/", json={"title": "Tarea a buscar"})
    task_id = post.json()["id"]

    response = client.get(f"/tasks/{task_id}")
    assert response.status_code == 200
    assert response.json()["title"] == "Tarea a buscar"


def test_get_nonexistent_task(client):
    """Debe devolver 404 si la tarea no existe."""
    response = client.get("/tasks/99999")
    assert response.status_code == 404


def test_update_task(client):
    """Debe actualizar una tarea existente."""
    post = client.post("/tasks/", json={"title": "Tarea a actualizar"})
    task_id = post.json()["id"]

    response = client.put(
        f"/tasks/{task_id}",
        json={"completed": True, "description": "Actualizada"},
    )
    assert response.status_code == 200
    assert response.json()["completed"] is True
    assert response.json()["description"] == "Actualizada"


def test_delete_task(client):
    """Debe eliminar una tarea y luego devolver 404 al buscarla."""
    post = client.post("/tasks/", json={"title": "Tarea a eliminar"})
    task_id = post.json()["id"]

    delete_response = client.delete(f"/tasks/{task_id}")
    assert delete_response.status_code == 204

    get_response = client.get(f"/tasks/{task_id}")
    assert get_response.status_code == 404