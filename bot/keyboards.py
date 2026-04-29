from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def main_menu():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="📥 Скачать Reel", callback_data="download")],
        [InlineKeyboardButton(text="ℹ️ Помощь", callback_data="help")]
    ])

def after_download():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="⬇️ Скачать ещё", callback_data="download")]
    ])