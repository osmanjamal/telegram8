from ..config import MENU_ITEMS

class MenuService:
    def get_menu(self):
        return MENU_ITEMS

    def get_item(self, item_id):
        return next((item for item in MENU_ITEMS if item['id'] == item_id), None)