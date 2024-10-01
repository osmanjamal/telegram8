from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from config import Config
from services.telegram_service import TelegramService
app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
CORS(app)

# Initialize services
telegram_service = TelegramService()

# Import models
from models import user, menu, order

# Import and register blueprints
from routes import auth_routes, menu_routes, order_routes, webhook_routes

app.register_blueprint(auth_routes.bp)
app.register_blueprint(menu_routes.bp)
app.register_blueprint(order_routes.bp)
app.register_blueprint(webhook_routes.bp)

if __name__ == '__main__':
    app.run(debug=True)