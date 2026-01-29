from aiogram import Bot, Dispatcher, F
from aiogram.types import (CallbackQuery, InlineKeyboardButton,
                           InlineKeyboardMarkup, InputMediaAudio,
                           InputMediaDocument, InputMediaPhoto,
                           InputMediaVideo, Message)
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.filters import CommandStart
from aiogram.exceptions import TelegramBadRequest
from env_names import bot_token

bot = Bot(bot_token)
dp = Dispatcher()

LEXICON: dict[str, str] = {
'audio': '🎶 Аудио',
    'text': '📃 Текст',
    'photo': '🖼 Фото',
    'video': '🎬 Видео',
    'document': '📑 Документ',
    'voice': '📢 Голосовое сообщение',
    'text_1': 'Это обыкновенное текстовое сообщение, его можно легко отредактировать другим текстовым сообщением, но нельзя отредактировать сообщением с медиа.',
    'text_2': 'Это тоже обыкновенное текстовое сообщение, которое можно заменить на другое текстовое сообщение через редактирование.',
    'photo_id1': 'AgACAgIAAxkBAAMdaXexo2FgpKi8Kcf-dXonswgAAV0zAAJYC2sbQejASzlG3IGrR4mpAQADAgADcwADOAQ',
    'photo_id2': 'AgACAgIAAxkBAAMtaXkJJaJgyBNfNtBaQjaSBOBKGToAAgQUaxuEPclLKhwx09fVciABAAMCAANzAAM4BA',
    'voice_id1': 'AwACAgIAAxkBAAM9aXkLNDsVV3WmnKrRRizJwkBRs3YAAruNAAKEPclLLo0ZYoDkzZM4BA',
    'voice_id2': 'AwACAgIAAxkBAAM_aXkLPV_o1B0SryZAy9xVOBxZdSYAAryNAAKEPclL9lsLvSWBcrQ4BA',
    'audio_id1': 'CQACAgIAAxkBAAMvaXkJ3X_u5VbQpgHF7Dr3tkQuf50AAqCNAAKEPclLiFQVRlPLjaw4BA',
    'audio_id2': 'CQACAgIAAxkBAAMxaXkKHOpRGrH387HYu3yyOKXsmKsAAqSNAAKEPclLpAfwSAnch_M4BA',
    'document_id1': 'BQACAgIAAxkBAAMgaXeyZVen9JT4_6rPe-PgH1bkNtEAAjCGAAJB6MBLAu5vlkdlbI44BA',
    'document_id2': 'BQACAgIAAxkBAAM1aXkKZEyCT-urHTBXIYtkflZUwxsAAqmNAAKEPclLp7x3rP5aYk04BA',
    'video_id1': 'BAACAgIAAxkBAAM5aXkK-ogAATX9zECI4l__XhPkeYKOAAItkAAC48_JS9ATX8ztY-T6OAQ',
    'video_id2': 'BAACAgIAAxkBAAM7aXkLBbB81u02FOUXaW-zmH_AL-0AAmyTAAM7uEvVStMDcp1vHTgE',
}


# Функция для генерации клавиатур с инлайн-кнопками
def get_markup(width: int, *args, **kwargs) -> InlineKeyboardMarkup:
    # Инициализируем билдер
    kb_builder = InlineKeyboardBuilder()
    # Инициализируем список для кнопок
    buttons: list[InlineKeyboardButton] = []
    # Заполняем список кнопками из аргументов args и kwargs
    if args:
        for button in args:
            buttons.append(InlineKeyboardButton(
                text=LEXICON[button] if button in LEXICON else button,
                callback_data=button
            ))
    if kwargs:
        for button, text in kwargs.items():
            buttons.append(InlineKeyboardButton(
                text=text,
                callback_data=button
            ))
    # Распаковываем список с кнопками в билдер методом row с параметром width
    kb_builder.row(*buttons, width=width)
    # Возвращаем объект инлайн-клавиатуры
    return kb_builder.as_markup()


@dp.message(CommandStart())
async def process_command_start(message: Message):
    markup = get_markup(2, 'video')
    await message.answer_audio(
        audio=LEXICON['audio_id1'],
        caption='Это audio 1',
        reply_markup=markup
    )


@dp.callback_query(F.data.in_(
    ['text', 'audio', 'video', 'document', 'photo', 'voice']
))
async def process_button_press(callback: CallbackQuery):

    # markup = get_markup(2, 'text')
    # if callback.message.text == LEXICON['text_1']:
    #     text = LEXICON['text_2']
    # else:
    #     text = LEXICON['text_1']
    # await callback.message.edit_text(
    #     text=text,
    #     reply_markup=markup
    # )

    try:
        markup = get_markup(2, 'audio')
        await callback.message.edit_media(
            media=InputMediaVideo(
                media=LEXICON['video_id1'],
                caption='Это video 1'
            ),
            reply_markup=markup
        )
    except TelegramBadRequest:
        markup = get_markup(2, 'video')
        await callback.message.edit_media(
            media=InputMediaAudio(
                media=LEXICON['audio_id1'],
                caption='Это audio 1'
            ),
            reply_markup=markup
        )


@dp.message()
async def send_echo(message: Message):
    await message.answer(text='Не понимаю')


if __name__ == '__main__':
    dp.run_polling(bot)
