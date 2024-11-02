from aiogram import Bot, Dispatcher
from aiogram.types import Message, InlineKeyboardButton,\
    InlineKeyboardMarkup, ReplyKeyboardRemove
from aiogram.filters import CommandStart

from my_config import BOT_TOKEN

bot = Bot(BOT_TOKEN)
dp = Dispatcher()

# kb_1
url_button_1 = InlineKeyboardButton(
    text='Курс "Телеграм-боты на Python и AIOgram"',
    url='https://stepik.org/120924'
)
url_button_2 = InlineKeyboardButton(
    text='Документация Telegram Bot API',
    url='https://core.telegram.org/bots/api'
)

keyboard_1 = InlineKeyboardMarkup(
    inline_keyboard=[[url_button_1],
                     [url_button_2]]
)

# kb_2
group_name = 'aiogram_stepik_course'
url_button_3 = InlineKeyboardButton(
    text='Группа "Телеграм-боты на AIOgram"',
    url=f'tg://resolve?domain={group_name}'
)
user_id = 5121827372
url_button_4 = InlineKeyboardButton(
    text='Автор курса на Степике по телеграм-ботам',
    url=f'tg://user?id={user_id}'
)
channel_name = 'toBeAnMLspecialist'
url_button_5 = InlineKeyboardButton(
    text='Канал "Стать специалистом по машинному обучению"',
    url=f'https://t.me/{channel_name}'
)

keyboard_2 = InlineKeyboardMarkup(
    inline_keyboard=[[url_button_3],
                     [url_button_4],
                     [url_button_5]]
)


@dp.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(
        text='Это инлайн-кнопки с параметром "url"',
        reply_markup=keyboard_2
    )


dp.run_polling(bot)
