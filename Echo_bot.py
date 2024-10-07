from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message
import config

BOT_TOKEN = config.BOT_TOKEN

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


# Этот хэндлер будет срабатывать на команду "/start"
async def process_start_command(message: Message):
    await message.answer('Привет!\nМеня зовут Эхо-бот!\nНапиши мне что-нибудь')


# Этот хэндлер будет срабатывать на команду "/help"
async def process_help_command(message: Message):
    await message.answer(
        'Напиши мне что-нибудь и в ответ '
        'я пришлю тебе твое сообщение'
    )


# Эти хэндлеры будут срабатывать на отправку различных медиа-файлов
async def send_photo_echo(message: Message):
    if message.photo:
        print("photo")
        await message.reply_photo(message.photo[0].file_id)


async def send_audio_echo(message: Message):
    if message.audio:
        print("audio")
        await message.reply_audio(message.audio.file_id)


async def send_video_echo(message: Message):
    if message.video:
        print("video")
        await message.reply_video(message.video.file_id)


async def send_sticker_echo(message: Message):
    if message.sticker:
        print("sticker")
        await message.reply_sticker(message.sticker.file_id)


@dp.message(F.animation)
async def send_animation_echo(message: Message):
    if message.animation:
        print("animation")
        await message.reply_animation(message.animation.file_id)


@dp.message(F.document)
async def send_document_echo(message: Message):
    if message.document:
        print("document")
        await message.reply_document(message.document.file_id)


@dp.message(F.voice)
async def send_voice_echo(message: Message):
    if message.voice:
        print("voice")
        await message.reply_voice(message.voice.file_id)


# Этот хэндлер будет срабатывать на любые текстовые сообщения
# кроме команд "/start" и "/help"
async def send_echo(message: Message):
    if message.text:
        print("text")
        await message.reply(text=message.text)


# Регистрируем хэндлеры
dp.message.register(process_start_command, Command(commands='start'))
dp.message.register(process_help_command, Command(commands='help'))
dp.message.register(send_photo_echo, F.photo)
dp.message.register(send_audio_echo, F.audio)
dp.message.register(send_video_echo, F.video)
dp.message.register(send_sticker_echo, F.sticker)
dp.message.register(send_echo)


if __name__ == '__main__':
    dp.run_polling(bot)
