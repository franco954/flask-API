import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../app')))

from app import app
import pytest

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'MicroApp Deploy API' in response.data

def test_health(client):
    response = client.get('/health')
    assert response.status_code == 200
    assert b'healthy' in response.data

def test_api_data(client):
    response = client.get('/api/data')
    assert response.status_code == 200
    data = response.get_json()
    assert len(data['data']) == 2