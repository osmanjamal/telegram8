from flask import Blueprint, request, jsonify
from models import User
from app import db
from services.auth_service import AuthService

bp = Blueprint('auth', __name__)
auth_service = AuthService()

@bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = auth_service.authenticate_user(data['telegram_id'])
    if user:
        token = auth_service.create_token(user)
        return jsonify({'token': token}), 200
    return jsonify({'message': 'Authentication failed'}), 401

@bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    user = auth_service.register_user(data)
    if user:
        return jsonify(user.to_dict()), 201
    return jsonify({'message': 'Registration failed'}), 400