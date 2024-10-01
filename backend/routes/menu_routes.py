from flask import Blueprint, jsonify
from models.menu import MenuItem

bp = Blueprint('menu', __name__)

@bp.route('/menu', methods=['GET'])
def get_menu():
    menu_items = MenuItem.query.all()
    return jsonify([item.to_dict() for item in menu_items])