import functools
import logging

def handle_errors(func):
    @functools.wraps(func)
    async def wrapper(update, context, *args, **kwargs):
        try:
            return await func(update, context, *args, **kwargs)
        except Exception as e:
            logging.error(f"حدث خطأ في {func.__name__}: {str(e)}")
            await update.message.reply_text("عذرًا، حدث خطأ. يرجى المحاولة مرة أخرى لاحقًا.")
    return wrapper