import random

from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from aiogram.filters import Command, CommandStart

from config import BOT_TOKEN

bot = Bot(BOT_TOKEN)
dp = Dispatcher()

ATTEMPTS = 5

users: dict = {}


def get_user(message: Message):
    if message.from_user:
        user = message.from_user
    if user.id not in users:
        print('\n', 'New user:', user.id, '\n')
        users[user.id] = {
            'in_game': False,
            'secret_number': 0,
            'attempts': 0,
            'total_games': 0,
            'wins': 0
            }
    return users[user.id]


def get_random_number() -> int:
    return random.randint(1, 100)


# /start
@dp.message(CommandStart())
async def process_start_command(message: Message):
    get_user(message)
    await message.answer(
        'Привет!\nДавай сыграем в игру "Угадай число"?\n\n'
        'Чтобы получить правила игры и список доступных '
        'команд - отправьте команду /help'
    )


# /help
@dp.message(Command(commands='help'))
async def process_help_command(message: Message):
    get_user(message)
    await message.answer(
        f'Правила игры:\n\nЯ загадываю число  от 1 до 100, '
        f'а вам нужно его угадать.\nУ вас есть {ATTEMPTS} '
        f'попыток\n\nДоступные команды:\n/help - правила '
        f'игры и список команд\n/cancel - выйти из игры\n'
        f'/stat - посмотреть статистику\n\nДавай сыграем?'
    )


# /stat
@dp.message(Command(commands='stat'))
async def process_stat_command(message: Message):
    user = get_user(message)
    await message.answer(
        f'Всего игр сыграно: {user["total_games"]}\n'
        f'Игр выиграно: {user["wins"]}'
    )


#   /cancel
@dp.message(Command(commands='cancel'))
async def process_cancel_command(message: Message):
    user = get_user(message)
    if user['in_game']:
        user['in_game'] = False
        await message.answer(
            'Вы вышли из игры. Если захотите сыграть '
            'снова - напишите об этом.'
        )
    else:
        await message.answer(
            'Мы еще не в игре. Может сыграем?'
        )


# yes
@dp.message(F.text.lower().in_(['да', 'давай', 'сыграем',
                                'игра', 'играть']))
async def process_positive_answer(message: Message):
    user = get_user(message)
    if not user['in_game']:
        user['in_game'] = True
        user['secret_number'] = get_random_number()
        user['attempts'] = ATTEMPTS
        await message.answer(
            'Ура!\n\nЯ загадал число от 1 до 100, '
            'попробуй угадать!'
        )
    else:
        await message.answer(
            'Пока мы играем в игру я могу'
            'реагировать только на числа от 1 до 100 '
            'и команды /cancel и /stat'
        )


# no
@dp.message(F.text.lower().in_(['нет', 'не', 'не хочу', 'не буду']))
async def process_negative_answer(message: Message):
    user = get_user(message)
    if not user['in_game']:
        await message.answer(
            'Жаль :(\n\nЕсли захотите поиграть - '
            'просто напишите об этом'
        )
    else:
        await message.answer(
            'Мы же сейчас с вами играем. Присылайте, '
            'пожалуйста, числа от 1 до 100'
        )


#   num
@dp.message(lambda x: x.text and x.text.isdigit()
            and 1 <= int(x.text) <= 100)
async def process_number_answer(message: Message):
    user = get_user(message)
    if user['in_game'] and message.text:
        if int(message.text) == user['secret_number']:
            user['in_game'] = False
            user['total_games'] += 1
            user['wins'] += 1
            await message.answer(
                'Ура!!! Вы угадали число!\n\n'
                'Может сыграем еще?'
            )
        elif int(message.text) > user['secret_number']:
            user['attempts'] -= 1
            await message.answer('Мое число меньше')
        elif int(message.text) < user['secret_number']:
            user['attempts'] -= 1
            await message.answer('Мое число больше')

        if user['attempts'] == 0:
            user['in_game'] = False
            user['total_games'] += 1
            await message.answer(
                f'К сожалению, у вас больше не осталось '
                f'попыток.\nВы проиграли:(\nМое число '
                f'было {user["secret_number"]}. \n\nДавайте '
                f'сыграем еще?'
            )
    else:
        await message.answer('Мы еще не играем. Хотите сыграть?')


#  any
@dp.message()
async def process_other_answers(message: Message):
    user = get_user(message)
    if user['in_game']:
        await message.answer(
            'Мы же с вами играем. '
            'Присылайте, пожалуйста, числа от 1 до 100.'
        )
    else:
        await message.answer(
            'Я довольно ограниченный бот, давайте '
            'просто сыграем в игру?'
        )


if __name__ == '__main__':
    dp.run_polling(bot)
