from flask import current_app
from models import get_user_model

class AuthService:
    @staticmethod
    def authenticate_user(username, password):
        User = get_user_model()
        user = User.query.filter_by(username=username).first()
        if user and user.check_password(password):
            return user
        return None

    @staticmethod
    def register_user(username, password, email):
        User = get_user_model()
        user = User(username=username, email=email)
        user.set_password(password)
        current_app.extensions['sqlalchemy'].db.session.add(user)
        current_app.extensions['sqlalchemy'].db.session.commit()
        return user