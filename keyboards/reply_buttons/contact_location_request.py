from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.types import (
    KeyboardButton,
    Message,
    ReplyKeyboardMarkup
)
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from env_names import bot_token

bot = Bot(token=bot_token)
dp = Dispatcher()

kb_builder = ReplyKeyboardBuilder()
contact_btn = KeyboardButton(
    text='Отправить телефон',
    request_contact=True
)
geo_btn = KeyboardButton(
    text='Отправить геолокацию',
    request_location=True
)
kb_builder.row(contact_btn, geo_btn, width=1)
keyboard: ReplyKeyboardMarkup = kb_builder.as_markup(
    resize_keyboard=True
)

@dp.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(
        text='Экспериментируем со специальными кнопками',
        reply_markup=keyboard
    )

@dp.message(F.contact)
async def process_contact(message: Message):
    await message.answer(
        text=f'Ваш телефон: {message.contact.phone_number}'
    )
    print(message.model_dump_json(indent=4, exclude_none=True))

@dp.message(F.location)
async def process_location(message: Message):
    await message.answer(
        text=f'Ваши координаты: {message.location.latitude, message.location.longitude}'
    )
    print(message.model_dump_json(indent=4, exclude_none=True))


if __name__ == '__main__':
    dp.run_polling(bot)
