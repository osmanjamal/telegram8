from flask import Blueprint, request, jsonify
from models import Order
from services.order_service import OrderService
from middleware.auth_middleware import token_required

bp = Blueprint('order', __name__)
order_service = OrderService()

@bp.route('/orders', methods=['POST'])
@token_required
def create_order(current_user):
    data = request.get_json()
    order = order_service.create_order(current_user.id, data)
    return jsonify(order.to_dict()), 201

@bp.route('/orders', methods=['GET'])
@token_required
def get_user_orders(current_user):
    orders = order_service.get_user_orders(current_user.id)
    return jsonify([order.to_dict() for order in orders]), 200

@bp.route('/orders/<int:order_id>', methods=['GET'])
@token_required
def get_order(current_user, order_id):
    order = order_service.get_order_by_id(order_id)
    if order and order.user_id == current_user.id:
        return jsonify(order.to_dict()), 200
    return jsonify({'message': 'Order not found'}), 404