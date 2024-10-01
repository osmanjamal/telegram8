# في الواقع، هذه الخدمة ستتعامل مع قاعدة بيانات
# هنا نستخدم قائمة بسيطة للتوضيح

orders = []

class OrderService:
    def create_order(self, user_id, items):
        order = {
            'id': len(orders) + 1,
            'user_id': user_id,
            'items': items,
            'total': sum(item['price'] * item['quantity'] for item in items),
            'status': 'جديد'
        }
        orders.append(order)
        return order

    def get_user_orders(self, user_id):
        return [order for order in orders if order['user_id'] == user_id]

    def update_order_status(self, order_id, status):
        for order in orders:
            if order['id'] == order_id:
                order['status'] = status
                return order
        return None