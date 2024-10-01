from telegram import Bot
from ..config import BOT_TOKEN

class TelegramService:
    def __init__(self):
        self.bot = Bot(token=BOT_TOKEN)

    async def send_message(self, chat_id, text):
        await self.bot.send_message(chat_id=chat_id, text=text)

    async def send_photo(self, chat_id, photo, caption=None):
        await self.bot.send_photo(chat_id=chat_id, photo=photo, caption=caption)

    async def send_invoice(self, chat_id, title, description, payload, provider_token, currency, prices):
        await self.bot.send_invoice(chat_id=chat_id, title=title, description=description,
                                    payload=payload, provider_token=provider_token,
                                    currency=currency, prices=prices)