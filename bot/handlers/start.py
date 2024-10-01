from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import ContextTypes
from ..config import WEBAPP_URL

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """إرسال رسالة عند إصدار الأمر /start."""
    user = update.effective_user
    web_app = WebAppInfo(url=WEBAPP_URL)
    keyboard = [
        [InlineKeyboardButton("افتح القائمة", web_app=web_app)],
        [InlineKeyboardButton("طلباتي", callback_data='my_orders')],
        [InlineKeyboardButton("حسابي", callback_data='my_account')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_html(
        rf"مرحبًا {user.mention_html()}! أهلاً بك في بوت بيت المحاشي. كيف يمكنني مساعدتك اليوم؟",
        reply_markup=reply_markup
    )