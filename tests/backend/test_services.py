import pytest
from app import app, db
from models import MenuItem, User
from services import MenuService, OrderService

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'

    with app.app_context():
        db.create_all()

    yield app

    with app.app_context():
        db.drop_all()

def test_menu_service(client):
    with app.app_context():
        menu_item = MenuItem(name='محشي ورق عنب', price=25.0, description='ورق عنب محشي بالأرز واللحم')
        db.session.add(menu_item)
        db.session.commit()

        menu_service = MenuService()
        items = menu_service.get_all_items()
        assert len(items) == 1
        assert items[0].name == 'محشي ورق عنب'

def test_order_service(client):
    with app.app_context():
        user = User(telegram_id=123456, name='Test User')
        menu_item = MenuItem(name='محشي ورق عنب', price=25.0)
        db.session.add(user)
        db.session.add(menu_item)
        db.session.commit()

        order_service = OrderService()
        order = order_service.create_order(user.id, {'items': [{'menu_item_id': menu_item.id, 'quantity': 2}]})
        assert order.total == 50.0
        assert len(order.items) == 1