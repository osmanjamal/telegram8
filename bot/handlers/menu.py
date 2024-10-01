from telegram import Update
from telegram.ext import ContextTypes
from ..config import MENU_ITEMS

async def menu(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """عرض قائمة الطعام."""
    menu_text = "قائمة الطعام:\n\n"
    for item in MENU_ITEMS:
        menu_text += f"{item['name']} - {item['price']} ريال\n{item['description']}\n\n"
    await update.message.reply_text(menu_text)