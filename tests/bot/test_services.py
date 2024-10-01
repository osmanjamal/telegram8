import pytest
from bot.services import menu_service, order_service

def test_get_menu():
    menu = menu_service.get_menu()
    assert isinstance(menu, list)
    assert len(menu) > 0
    assert "name" in menu[0]
    assert "price" in menu[0]

def test_create_order():
    user_id = 123456
    items = [{"menu_item_id": 1, "quantity": 2}]
    order = order_service.create_order(user_id, items)
    assert order['user_id'] == user_id
    assert len(order['items']) == 1
    assert order['items'][0]['quantity'] == 2