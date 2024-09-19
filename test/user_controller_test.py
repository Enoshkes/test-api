import pytest
from flask import Flask
from controllers.user_controller import user_blueprint  # Replace 'your_module' with the actual module name

@pytest.fixture
def app():
    app = Flask(__name__)
    app.register_blueprint(user_blueprint)
    return app

@pytest.fixture
def client(app):
    return app.test_client()

def test_search_user(client):
    response = client.get('/search?name=John&age=30')
    assert response.status_code == 200
    data = response.get_json()
    assert data == {'name': 'John', 'age': '30'}