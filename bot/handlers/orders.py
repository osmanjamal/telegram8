from telegram import Update
from telegram.ext import ContextTypes
from ..services import order_service

async def orders(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """عرض طلبات المستخدم."""
    user_id = update.effective_user.id
    orders = order_service.get_user_orders(user_id)
    
    if not orders:
        await update.message.reply_text("ليس لديك أي طلبات حالية.")
        return

    orders_text = "طلباتك:\n\n"
    for order in orders:
        orders_text += f"رقم الطلب: {order['id']}\n"
        orders_text += f"الحالة: {order['status']}\n"
        orders_text += f"المجموع: {order['total']} ريال\n\n"

    await update.message.reply_text(orders_text)