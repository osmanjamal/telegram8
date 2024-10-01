from app import Config

class PaymentService:
    @staticmethod
    def process_payment(order, payment_data):
        # هنا يمكنك إضافة منطق معالجة الدفع
        # هذا مثال بسيط، في الواقع ستحتاج إلى التكامل مع بوابة دفع حقيقية
        if payment_data['amount'] == order.total:
            return True
        return False

    @staticmethod
    def create_invoice(order):
        # إنشاء فاتورة لـ Telegram Payments
        return {
            "title": f"طلب رقم {order.id}",
            "description": f"دفع لطلب من بيت المحاشي",
            "payload": str(order.id),
            "provider_token": Config.PAYMENT_PROVIDER_TOKEN,
            "start_parameter": f"order_{order.id}",
            "currency": "SAR",
            "prices": [{"label": "المجموع", "amount": int(order.total * 100)}]
        }