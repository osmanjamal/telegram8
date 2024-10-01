from models import Order, OrderItem, MenuItem
from app import db

class OrderService:
    @staticmethod
    def create_order(user_id, data):
        order = Order(user_id=user_id, total=0)
        db.session.add(order)
        
        total = 0
        for item in data['items']:
            menu_item = MenuItem.query.get(item['menu_item_id'])
            if menu_item:
                order_item = OrderItem(
                    order_id=order.id,
                    menu_item_id=menu_item.id,
                    quantity=item['quantity']
                )
                db.session.add(order_item)
                total += menu_item.price * item['quantity']
        
        order.total = total
        db.session.commit()
        return order

    @staticmethod
    def get_user_orders(user_id):
        return Order.query.filter_by(user_id=user_id).all()

    @staticmethod
    def get_order_by_id(order_id):
        return Order.query.get(order_id)

    @staticmethod
    def update_order_status(order_id, status):
        order = Order.query.get(order_id)
        if order:
            order.status = status
            db.session.commit()
        return order