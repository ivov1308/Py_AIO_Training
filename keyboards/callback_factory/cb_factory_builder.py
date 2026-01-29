from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.filters.callback_data import CallbackData
from aiogram.types import (CallbackQuery, Message)
from aiogram.utils.keyboard import InlineKeyboardBuilder
from my_config import BOT_TOKEN

bot = Bot(BOT_TOKEN)
dp = Dispatcher()


class GoodsCallbackFactory(CallbackData, prefix='goods'):
    category_id: int
    subcategory_id: int
    item_id: int


builder = InlineKeyboardBuilder()


for i in range(2):
    builder.button(
        text=f'Категория {i+1}',
        callback_data=GoodsCallbackFactory(
            category_id=i+1,
            subcategory_id=0,
            item_id=0
        )
    )

builder.adjust(1)


@dp.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(
        text='Вот такая клавиатура',
        reply_markup=builder.as_markup()
    )


@dp.callback_query(GoodsCallbackFactory.filter())
async def process_category_press(callback: CallbackQuery,
                                 callback_data: GoodsCallbackFactory):
    await callback.message.answer(
        text=callback_data.pack()
    )
    await callback.answer()


dp.run_polling(bot)
