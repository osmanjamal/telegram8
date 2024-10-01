from flask import Blueprint, request, jsonify
from services.telegram_service import TelegramService

bp = Blueprint('webhook', __name__)
telegram_service = TelegramService()

@bp.route('/webhook', methods=['POST'])
def handle_webhook():
    update = request.get_json()
    telegram_service.process_update(update)
    return jsonify({'status': 'ok'}), 200