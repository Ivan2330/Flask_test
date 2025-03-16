import pytest
import os
import sys

sys.path.append("/app")

from main import app
from app.models import db, User

@pytest.fixture(scope="module")
def test_client():
    app.config["TESTING"] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("TEST_DATABASE_URL", "postgresql://flask_user:password@test_db/flask_users_test_db")

    with app.test_client() as testing_client:
        with app.app_context():
            db.create_all()  
        yield testing_client
        with app.app_context():
            db.drop_all()

def test_create_user(test_client):
    """creating user test"""
    response = test_client.post("/users", json={"name": "Ivan", "email": "ivan@example.com"})
    assert response.status_code == 201
    assert response.json["name"] == "Ivan"

def test_get_users(test_client):
    """Getting all users"""
    response = test_client.get("/users")
    assert response.status_code == 200
    assert any(user["email"] == "ivan@example.com" for user in response.json["users"])

def test_get_user_by_id(test_client):
    """Getting user by id"""
    response = test_client.get("/users/1")
    assert response.status_code == 200
    assert response.json["name"] == "Ivan"

def test_update_user(test_client):
    """Updating user data"""
    response = test_client.put("/users/1", json={"name": "Updated Ivan", "email": "ivan@example.com"})
    assert response.status_code == 200
    assert response.json["name"] == "Updated Ivan"

def test_delete_user(test_client):
    """Deleting user"""
    response = test_client.delete("/users/1")
    assert response.status_code == 200

    response = test_client.get("/users/1")
    assert response.status_code == 404
