# مشروع بوت مطعم بيت المحاشي

هذا المشروع هو بوت تيليجرام مع تطبيق ويب مدمج لمطعم بيت المحاشي. يتيح للزبائن استعراض القائمة وتقديم الطلبات وتتبع حالة الطلبات.

## المميزات

- بوت تيليجرام للتفاعل مع الزبائن
- تطبيق ويب مدمج لعرض القائمة وتقديم الطلبات
- نظام إدارة للطلبات والمستخدمين
- دعم الدفع عبر تيليجرام

## المتطلبات

- Python 3.9+
- Node.js 14+
- PostgreSQL
- Docker و Docker Compose (للنشر)

## التثبيت والتشغيل

1. استنسخ المستودع:
   ```
   git clone https://github.com/your-username/beit-almahashi-bot.git
   cd beit-almahashi-bot
   ```

2. قم بإنشاء ملف `.env` وأضف المتغيرات البيئية اللازمة (انظر إلى ملف `.env.example` للاطلاع على المتغيرات المطلوبة).

3. قم بتشغيل المشروع باستخدام Docker Compose:
   ```
   docker-compose up --build
   ```

## الاختبارات

لتشغيل الاختبارات:

```
# اختبارات البوت
pytest tests/bot

# اختبارات تطبيق الويب
cd web_app && npm test

# اختبارات الباك إند
pytest tests/backend
```

## هيكل المشروع

```
beit-almahashi/
├── bot/                # كود بوت التيليجرام
├── web_app/            # تطبيق الويب (React)
├── backend/            # خدمة الباك إند (Flask)
├── tests/              # اختبارات
├── docker/             # ملفات Docker
├── docker-compose.yml
├── .env.example
├── requirements.txt
└── README.md
```

## المساهمة

نرحب بالمساهمات! يرجى اتباع الخطوات التالية:

1. قم بعمل fork للمشروع
2. قم بإنشاء فرع جديد (`git checkout -b feature/AmazingFeature`)
3. قم بعمل commit للتغييرات (`git commit -m 'Add some AmazingFeature'`)
4. قم بدفع الفرع (`git push origin feature/AmazingFeature`)
5. قم بفتح طلب سحب

## الترخيص

هذا المشروع مرخص تحت رخصة MIT. انظر إلى ملف `LICENSE` للمزيد من التفاصيل.

## الاتصال

اسم المطور - [@your_twitter](https://twitter.com/your_twitter)

رابط المشروع: [https://github.com/your-username/beit-almahashi-bot](https://github.com/your-username/beit-almahashi-bot)