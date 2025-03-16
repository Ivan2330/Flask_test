from flask import Blueprint, jsonify, request
from sqlalchemy.orm import Session
from app.models import db, User
from app.schemas import UserCreate, UserUpdate, UserResponse, UserListResponse
from flask_pydantic import validate

user_routes = Blueprint("users", __name__)

@user_routes.route("/users", methods=["POST"])
@validate()
def add_user(body: UserCreate):
    """Creating new user"""
    with Session(db.engine) as session:
        new_user = User(name=body.name, email=body.email)
        session.add(new_user)
        session.commit()
        session.refresh(new_user)
    return UserResponse(id=new_user.id, name=new_user.name, email=new_user.email, created_at=new_user.created_at).model_dump(), 201

@user_routes.route("/users", methods=["GET"])
def get_users():
    """Getting all users"""
    with Session(db.engine) as session:
        users = session.query(User).all()
    return UserListResponse(users=[UserResponse(id=u.id, name=u.name, email=u.email, created_at=u.created_at) for u in users]).model_dump()

@user_routes.route("/users/<int:id>", methods=["GET"])
def get_user(id):
    """Getting user"""
    with Session(db.engine) as session:
        user = session.get(User, id)
        if user is None:
            return jsonify({"error": "User not found"}), 404
    return UserResponse(id=user.id, name=user.name, email=user.email, created_at=user.created_at).model_dump()

@user_routes.route("/users/<int:id>", methods=["PUT"])
@validate()
def update_user(id: int, body: UserUpdate):
    """Updating user"""
    with Session(db.engine) as session:
        user = session.get(User, id)
        if user is None:
            return jsonify({"error": "User not found"}), 404
        if body.name:
            user.name = body.name
        if body.email:
            user.email = body.email
        session.commit()
        session.refresh(user)
    return UserResponse(id=user.id, name=user.name, email=user.email, created_at=user.created_at).model_dump()

@user_routes.route("/users/<int:id>", methods=["DELETE"])
def delete_user(id):
    """Deleting user"""
    with Session(db.engine) as session:
        user = session.get(User, id)
        if user is None:
            return jsonify({"error": "User not found"}), 404
        session.delete(user)
        session.commit()
    return jsonify({"message": "User deleted successfully"}), 200
