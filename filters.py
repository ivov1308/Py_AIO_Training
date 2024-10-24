from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, ChatMemberUpdated
from aiogram.filters import ChatMemberUpdatedFilter, KICKED, BaseFilter

from my_config import BOT_TOKEN

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


# my filters #


def my_start_filter(message: Message) -> bool:
    return message.text == '/start'


@dp.message(my_start_filter)
async def process_start_command(message: Message):
    await message.answer(text='Это команда /start')


@dp.my_chat_member(ChatMemberUpdatedFilter(member_status_changed=KICKED))
async def process_user_blooked_bot(event: ChatMemberUpdated):
    print(f'Пользователь {event.from_user.id} заблокировал бота')


# admin filter #


admin_ids: list[int] = [5121827372]


class IsAdmin(BaseFilter):
    def __init__(self, admin_ids: list[int]) -> None:
        self.admin_ids = admin_ids

    async def __call__(self, message: Message) -> bool:
        return message.from_user.id in self.admin_ids


@dp.message(IsAdmin(admin_ids))
async def admin_answer(message: Message):
    await message.answer(
        text='Приветствую тебя, Одмэн - властелин программы сей')


@dp.message()
async def other_answer(message: Message):
    print(message.from_user.id)
    await message.answer(text='Чего тебе, простолюдин?!')


# filter with argument #


class NumbersInMessage(BaseFilter):
    async def __call__(self, message: Message) -> bool | dict[str, list[int]]:
        numbers = []
        for word in message.text.split():
            num = ''
            for char in word:
                if char.isdigit():
                    num += char
            if num:
                numbers.append(int(num))
        if numbers:
            return {'numbers': numbers}
        return False


@dp.message(F.text.lower().startswith('найди числа'),
            NumbersInMessage())
async def process_if_numbers(message: Message, numbers: list[int]):
    await message.answer(
        text=f'Нашел: {", ".join(str(num) for num in numbers)}')


@dp.message(F.text.lower().startswith('найди числа'))
async def process_if_not_numbers(message: Message):
    await message.answer(text='Не нашел что-то :(')

if __name__ == '__main__':
    dp.run_polling(bot)
