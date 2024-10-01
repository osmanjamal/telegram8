from telegram import InlineKeyboardButton, InlineKeyboardMarkup

def get_order_menu_keyboard(order_id):
    keyboard = [
        [InlineKeyboardButton("تأكيد الطلب", callback_data=f'confirm_order:{order_id}')],
        [InlineKeyboardButton("إلغاء الطلب", callback_data=f'cancel_order:{order_id}')],
        [InlineKeyboardButton("العودة للقائمة الرئيسية", callback_data='main_menu')]
    ]
    return InlineKeyboardMarkup(keyboard)