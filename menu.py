from aiogram import Bot, Dispatcher
from aiogram.types import Message, BotCommand
from aiogram.filters import Command

from my_config import BOT_TOKEN

my_bot = Bot(BOT_TOKEN)
dp = Dispatcher()


async def set_main_menu(bot: Bot):  # Аргумент строго "bot"!

    main_menu_commands = [
        BotCommand(command='/help',
                   description='Справка по работе бота'),
        BotCommand(command='/support',
                   description='Поддержка'),
        BotCommand(command='/contacts',
                   description='Другие способы связи'),
        BotCommand(command='/payments',
                   description='Платежи'),
    ]

    await bot.set_my_commands(main_menu_commands)


# Хэндлер удаления кнопки меню
@dp.message(Command(commands='delmenu'))
async def del_main_menu(message: Message, bot: Bot):
    await bot.delete_my_commands()
    await message.answer(text='Кнопка "Menu" удалена')


dp.startup.register(set_main_menu)
dp.run_polling(my_bot)
