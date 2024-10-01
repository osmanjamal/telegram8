import os
from dotenv import load_dotenv

# تحميل المتغيرات البيئية
load_dotenv()

# توكن البوت
BOT_TOKEN = "7363207789:AAG27mLEwz-q9L8puYKh5vXDVbsGez7gtKs"

# رابط تطبيق الويب
WEBAPP_URL = os.getenv('WEBAPP_URL', 'https://your-webapp-url.com')

# معرف قناة الإشعارات
NOTIFICATION_CHANNEL_ID = os.getenv('NOTIFICATION_CHANNEL_ID')

# معلومات قاعدة البيانات
DATABASE_URL = os.getenv('DATABASE_URL', 'sqlite:///bot.db')

# قائمة الطعام (يمكن نقلها إلى قاعدة البيانات لاحقاً)
MENU_ITEMS = [
    {
        "id": 1,
        "name": "محشي ورق عنب",
        "description": "ورق عنب محشي بالأرز واللحم المفروم",
        "price": 25.00,
        "image_url": "https://example.com/images/grape-leaves.jpg"
    },
    {
        "id": 2,
        "name": "محشي كوسا",
        "description": "كوسا محشية بالأرز واللحم المفروم",
        "price": 30.00,
        "image_url": "https://example.com/images/stuffed-zucchini.jpg"
    },
    {
        "id": 3,
        "name": "محشي باذنجان",
        "description": "باذنجان محشي بالأرز والصنوبر",
        "price": 28.00,
        "image_url": "https://example.com/images/stuffed-eggplant.jpg"
    }
]