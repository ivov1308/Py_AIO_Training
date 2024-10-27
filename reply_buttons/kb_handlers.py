from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import (Message, ReplyKeyboardRemove)

from my_config import BOT_TOKEN
from reply_keyboards import *

bot = Bot(BOT_TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(
        text='Добро пожаловать в обозреватель клавиатур!\n\n'
             '/start - начальное меню\n'
             '/stop - убрать клавиатуру\n\n'
             'Выберите клавиатуру для демонстрации:\n'
             '1 - Вопрос про кошек (2 кнопки)\n'
             '2 - Клавиатура 3х3\n'
             '3 - Клавиатура ромбиком (9 кнопок)\n'
             '4 - Клавиатура 25х12 (300 кнопок - max!)\n'
             '5 - kb_builder_1 (row4+row3)\n'
             '6 - kb_builder_2 (row4+add)\n'
             '7 - Специальные кнопки',
        reply_markup=keyboard_start
    )


@dp.message(Command(commands='stop'))
async def process_start_command(message: Message):
    await message.answer(
        text='Клавиатура закрыта',
        reply_markup=ReplyKeyboardRemove()
    )


@dp.message(F.text == '1')
async def process_keyboard_1(message: Message):
    await message.answer(
        text='Чего кошки боятся больше?',
        reply_markup=keyboard_1
    )

@dp.message(F.text == 'Собак 🦮')
async def process_dog_answer(message: Message):
    await message.answer(
        text='Да, несомненно, кошки боятся собак. '
             'Но вы видели как они боятся огурцов?'
    )

@dp.message(F.text == 'Огурцов 🥒')
async def process_cucumber_answer(message: Message):
    await message.answer(
        text='Да, иногда кажется, что огурцов '
             'кошки боятся больше'
    )


@dp.message(F.text == '2')
async def process_keyboard_2(message: Message):
    await message.answer(
        text='Клавиатура 3х3',
        reply_markup=keyboard_2)


@dp.message(F.text == '3')
async def process_keyboard_3(message: Message):
    await message.answer(
        text='Клавиатура ромбиком',
        reply_markup=keyboard_3
    )


@dp.message(F.text == '4')
async def process_keyboard_4(message: Message):
    await message.answer(
        text='Клавиатура 25х12',
        reply_markup=keyboard_4
    )


@dp.message(F.text == '5')
async def process_keyboard_5(message: Message):
    await message.answer(
        text='kb_builder_1 (row4+row3)',
        reply_markup=keyboard_5
    )


@dp.message(F.text == '6')
async def process_keyboard_6(message: Message):
    await message.answer(
        text='kb_builder_2 (row4+add)',
        reply_markup=keyboard_6
    )


@dp.message(F.text == '7')
async def process_keyboard_7(message: Message):
    await message.answer(
        text='Специальные кнопки',
        reply_markup=keyboard_7
    )


if __name__ == '__main__':
    dp.run_polling(bot)
