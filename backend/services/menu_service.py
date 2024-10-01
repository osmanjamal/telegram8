from models import MenuItem
from app import db

class MenuService:
    @staticmethod
    def get_all_items():
        return MenuItem.query.all()

    @staticmethod
    def get_item_by_id(item_id):
        return MenuItem.query.get(item_id)

    @staticmethod
    def create_item(data):
        item = MenuItem(
            name=data['name'],
            description=data.get('description'),
            price=data['price'],
            image_url=data.get('image_url'),
            category=data.get('category')
        )
        db.session.add(item)
        db.session.commit()
        return item

    @staticmethod
    def update_item(item_id, data):
        item = MenuItem.query.get(item_id)
        if item:
            item.name = data.get('name', item.name)
            item.description = data.get('description', item.description)
            item.price = data.get('price', item.price)
            item.image_url = data.get('image_url', item.image_url)
            item.category = data.get('category', item.category)
            db.session.commit()
        return item