import pytest
from unittest.mock import AsyncMock, patch
from telegram import Update
from telegram.ext import ContextTypes
from bot.handlers import start, menu

@pytest.fixture
def update():
    return AsyncMock(spec=Update)

@pytest.fixture
def context():
    return AsyncMock(spec=ContextTypes.DEFAULT_TYPE)

@pytest.mark.asyncio
async def test_start_command(update, context):
    update.effective_user.mention_html.return_value = "User"
    await start(update, context)
    update.message.reply_html.assert_called_once()
    assert "مرحبًا User" in update.message.reply_html.call_args[0][0]

@pytest.mark.asyncio
@patch('bot.handlers.menu_service.get_menu')
async def test_menu_command(mock_get_menu, update, context):
    mock_get_menu.return_value = [
        {"name": "محشي ورق عنب", "price": 25.0},
        {"name": "محشي كوسا", "price": 30.0}
    ]
    await menu(update, context)
    update.message.reply_text.assert_called_once()
    assert "محشي ورق عنب" in update.message.reply_text.call_args[0][0]
    assert "محشي كوسا" in update.message.reply_text.call_args[0][0]