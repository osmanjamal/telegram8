from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from ..utils.constants import MENU_BUTTON, ORDERS_BUTTON, ACCOUNT_BUTTON
from ..config import WEBAPP_URL

def get_main_menu_keyboard():
    keyboard = [
        [InlineKeyboardButton(MENU_BUTTON, web_app=WEBAPP_URL)],
        [InlineKeyboardButton(ORDERS_BUTTON, callback_data='my_orders')],
        [InlineKeyboardButton(ACCOUNT_BUTTON, callback_data='my_account')]
    ]
    return InlineKeyboardMarkup(keyboard)