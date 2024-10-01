import jwt
from datetime import datetime, timedelta
from models import User
from app import db, Config

class AuthService:
    @staticmethod
    def authenticate_user(telegram_id):
        return User.query.filter_by(telegram_id=telegram_id).first()

    @staticmethod
    def create_token(user):
        token = jwt.encode({
            'user_id': user.id,
            'exp': datetime.utcnow() + timedelta(hours=24)
        }, Config.JWT_SECRET_KEY)
        return token

    @staticmethod
    def register_user(data):
        user = User(
            telegram_id=data['telegram_id'],
            username=data.get('username'),
            name=data.get('name'),
            phone=data.get('phone'),
            address=data.get('address')
        )
        db.session.add(user)
        db.session.commit()
        return user

    @staticmethod
    def verify_token(token):
        try:
            data = jwt.decode(token, Config.JWT_SECRET_KEY, algorithms=["HS256"])
            return User.query.get(data['user_id'])
        except:
            return None