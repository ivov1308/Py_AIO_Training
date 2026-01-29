from aiogram import Bot, Dispatcher
from aiogram.types import Message
from env_names import bot_token
import json

bot = Bot(bot_token)
dp = Dispatcher()


@dp.message()
async def get_file_id(message: Message):

    file_type = message.content_type.split('.')[-1].lower()

    if file_type == 'photo':
        file_name = message.photo[0].file_unique_id
        file_id = message.photo[0].file_id
    elif file_type == 'voice':
        file_name = message.voice.file_unique_id
        file_id = message.voice.file_id
    elif file_type in ['audio', 'document', 'video']:
        file_name = eval(f"message.{file_type}.file_name")
        file_id = eval(f"message.{file_type}.file_id")
    else:
        await message.answer('Неподдерживаемый тип файла')
        return

    with open('file_ids.json', 'r') as f:
        file_ids: dict[str, dict[str, str]] = json.load(f)
        if file_name in file_ids.setdefault(file_type, dict()):
            await message.answer('Файл уже был добавлен!')
            return

    file_ids[file_type][file_name] = file_id

    with open('file_ids.json', 'w') as f:
        json.dump(file_ids, f, ensure_ascii=False, indent=4)
    await message.answer(text=f'{file_type}_{file_name}_id добавлено!')


if __name__ == '__main__':
    dp.run_polling(bot)
