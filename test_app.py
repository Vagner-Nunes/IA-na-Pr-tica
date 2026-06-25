import pytest
from app import app, tasks

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

# Gerado com o prompt do GitHub Copilot:
# "Escreva testes unitários utilizando pytest para a rota POST '/tasks'. Teste um cenário de sucesso enviando o título e um cenário de falha enviando um payload vazio."
def test_create_task_success(client):
    response = client.post('/tasks', json={"title": "Nova Tarefa de Teste"})
    assert response.status_code == 201
    assert response.json['title'] == "Nova Tarefa de Teste"
    assert response.json['completed'] is False

def test_create_task_missing_title(client):
    response = client.post('/tasks', json={})
    assert response.status_code == 400
    assert "O título é obrigatório" in response.json['error']
