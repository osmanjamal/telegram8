def get_user_model():
    from .user import User
    return User

def get_menu_model():
    from .menu import MenuItem
    return MenuItem

def get_order_model():
    from .order import Order
    return Order