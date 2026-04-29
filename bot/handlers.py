from aiogram import Router
from aiogram.types import Message, FSInputFile
from bot.downloader import download_media

router = Router()


@router.message()
async def handle(message: Message):
    url = message.text

    if "instagram.com" not in url:
        await message.answer("❌ Отправь Instagram ссылку")
        return

    await message.answer("⏳ Скачиваю...")

    try:
        files = download_media(url)

        for f in files:
            if f.endswith(".mp4"):
                await message.answer_video(FSInputFile(f))
            else:
                await message.answer_photo(FSInputFile(f))

    except:
        await message.answer("❌ Ошибка загрузки, попробуй позже")