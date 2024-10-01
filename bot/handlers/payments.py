from telegram import Update
from telegram.ext import ContextTypes
from ..services import order_service

async def handle_successful_payment(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """معالجة الدفع الناجح."""
    successful_payment = update.message.successful_payment
    order_id = successful_payment.invoice_payload
    
    # تحديث حالة الطلب
    order_service.update_order_status(order_id, "تم الدفع")
    
    await update.message.reply_text(
        f"شكراً لك! تم استلام دفعتك بنجاح للطلب رقم {order_id}. "
        "سيتم تحضير طلبك قريباً."
    )