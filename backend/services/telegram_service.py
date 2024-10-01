import logging
from telegram import Bot
from telegram.error import TelegramError
from config import Config

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class TelegramService:
    def __init__(self):
        try:
            self.bot = Bot(token=Config.BOT_TOKEN)
            logger.info("TelegramService initialized successfully")
        except Exception as e:
            logger.error(f"Failed to initialize TelegramService: {str(e)}")
            self.bot = None

    async def send_message(self, chat_id, text):
        if not self.bot:
            logger.error("Bot is not initialized. Cannot send message.")
            return

        try:
            await self.bot.send_message(chat_id=chat_id, text=text)
            logger.info(f"Message sent to chat_id: {chat_id}")
        except TelegramError as e:
            logger.error(f"Failed to send message: {str(e)}")

    # Add other methods as needed