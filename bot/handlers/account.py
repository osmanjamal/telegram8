from telegram import Update
from telegram.ext import ContextTypes
from ..services import user_service

async def account(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """عرض معلومات حساب المستخدم."""
    user_id = update.effective_user.id
    user_info = user_service.get_user_info(user_id)
    
    if not user_info:
        await update.message.reply_text("لم يتم العثور على معلومات الحساب. يرجى التسجيل أولاً.")
        return

    account_text = f"معلومات حسابك:\n\n"
    account_text += f"الاسم: {user_info['name']}\n"
    account_text += f"رقم الهاتف: {user_info['phone']}\n"
    account_text += f"العنوان: {user_info['address']}\n"

    await update.message.reply_text(account_text)