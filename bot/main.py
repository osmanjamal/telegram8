import logging
from telegram.ext import Application, CommandHandler, MessageHandler, filters
from config import BOT_TOKEN
from handlers import start, menu, orders, account, payments, web_app

# إعداد التسجيل
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)

def main() -> None:
    """تشغيل البوت."""
    # إنشاء التطبيق وتمرير توكن البوت
    application = Application.builder().token(BOT_TOKEN).build()

    # إضافة المعالجات
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("menu", menu))
    application.add_handler(CommandHandler("orders", orders))
    application.add_handler(CommandHandler("account", account))
    application.add_handler(MessageHandler(filters.SUCCESSFUL_PAYMENT, payments.handle_successful_payment))
    application.add_handler(MessageHandler(filters.StatusUpdate.WEB_APP_DATA, web_app.handle_webapp_data))

    # بدء البوت
    application.run_polling()

if __name__ == '__main__':
    main()