import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

import pytest
from app.app import app  # Importa la aplicación Flask

@pytest.fixture
def client():
    # Configura el cliente de prueba para Flask
    with app.test_client() as client:
        yield client

def test_multiply(client):
    # Caso feliz
    response = client.get('/multiply?num1=3&num2=5')
    assert response.status_code == 200
    assert response.json['result'] == 15

    # Entrada no válida
    response = client.get('/multiply?num1=3&num2=abc')
    assert response.status_code == 400

def test_divide(client):
    # Caso feliz
    response = client.get('/divide?num1=10&num2=2')
    assert response.status_code == 200
    assert response.json['result'] == 5

    # División por cero
    response = client.get('/divide?num1=10&num2=0')
    assert response.status_code == 406
    assert response.json['error'] == "Division by zero is not allowed"

    # Entrada no válida
    response = client.get('/divide?num1=10&num2=abc')
    assert response.status_code == 400
