import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
CORS(app)

# تأخير استيراد النماذج والمسارات
with app.app_context():
    from models import get_user_model, get_menu_model, get_order_model
    from routes import auth_routes, menu_routes, order_routes, webhook_routes
    from services.telegram_service import TelegramService

    # Initialize services
    telegram_service = TelegramService()

    # Register blueprints
    app.register_blueprint(auth_routes.bp)
    app.register_blueprint(menu_routes.bp)
    app.register_blueprint(order_routes.bp)
    app.register_blueprint(webhook_routes.bp)

if __name__ == '__main__':
    app.run(debug=True)