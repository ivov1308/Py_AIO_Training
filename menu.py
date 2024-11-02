from aiogram import Bot, Dispatcher
from aiogram.types import Message, BotCommand, ReplyKeyboardRemove
from aiogram.filters import Command

from my_config import BOT_TOKEN

my_bot = Bot(BOT_TOKEN)
dp = Dispatcher()


async def set_main_menu(bot: Bot):  # Аргумент строго "bot"!

    main_menu_commands = [
        BotCommand(command='/start',
                   description='Начало работы бота'),
        BotCommand(command='/help',
                   description='Справка по работе бота'),
        BotCommand(command='/delkb',
                   description='Удалить клавиатуру'),
        BotCommand(command='/delmenu',
                   description='Удаление кнопки "Меню"')
    ]

    await bot.set_my_commands(main_menu_commands)


@dp.message(Command(commands='delmenu'))
async def del_main_menu(message: Message, bot: Bot):
    await bot.delete_my_commands()
    await message.answer(text='Кнопка "Menu" удалена')


@dp.message(Command(commands='delkb'))
async def del_main_menu(message: Message, bot: Bot):
    await message.answer(text='Клавиатура удалена',
                         reply_markup=ReplyKeyboardRemove())


dp.startup.register(set_main_menu)
dp.run_polling(my_bot)
