import json
from telegram import Update
from telegram.ext import ContextTypes
from ..services import order_service

async def handle_webapp_data(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """معالجة البيانات المرسلة من تطبيق الويب."""
    data = json.loads(update.effective_message.web_app_data.data)
    user_id = update.effective_user.id
    
    if data['action'] == 'place_order':
        order = order_service.create_order(user_id, data['items'])
        await update.message.reply_text(f"تم استلام طلبك! رقم الطلب: {order['id']}")
    elif data['action'] == 'update_account':
        # تحديث معلومات الحساب
        # يمكن إضافة هذه الوظيفة لاحقاً
        pass