import pytest
from flask import json
from app import app, db
from models import MenuItem, User

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    client = app.test_client()

    with app.app_context():
        db.create_all()

    yield client

    with app.app_context():
        db.drop_all()

def test_get_menu(client):
    with app.app_context():
        menu_item = MenuItem(name='محشي ورق عنب', price=25.0, description='ورق عنب محشي بالأرز واللحم')
        db.session.add(menu_item)
        db.session.commit()

    response = client.get('/api/menu')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert len(data) == 1
    assert data[0]['name'] == 'محشي ورق عنب'

def test_create_order(client):
    with app.app_context():
        user = User(telegram_id=123456, name='Test User')
        menu_item = MenuItem(name='محشي ورق عنب', price=25.0)
        db.session.add(user)
        db.session.add(menu_item)
        db.session.commit()

    response = client.post('/api/orders', json={
        'user_id': user.id,
        'items': [{'menu_item_id': menu_item.id, 'quantity': 2}]
    })
    assert response.status_code == 201
    data = json.loads(response.data)
    assert data['total'] == 50.0
    assert len(data['items']) == 1