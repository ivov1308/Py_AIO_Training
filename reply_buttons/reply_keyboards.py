from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder, KeyboardButtonPollType
from aiogram.types.web_app_info import WebAppInfo

# keyboard_start
buttons_start: list[list[KeyboardButton]] = [
    [KeyboardButton(text=f'{i + 1}') for i in range(7)]
]
keyboard_start = ReplyKeyboardMarkup(
    keyboard=buttons_start,
    resize_keyboard=True,
    input_field_placeholder='Сюда вставится текст кнопки'
)


# keyboard_1
button_dog = KeyboardButton(text='Собак 🦮')
button_cuc = KeyboardButton(text='Огурцов 🥒')
keyboard_1 = ReplyKeyboardMarkup(
    keyboard=[[button_dog, button_cuc]],
    resize_keyboard=True,
    one_time_keyboard=True
)


# keyboard_2
buttons_2: list[list[KeyboardButton]] = [[KeyboardButton(
    text=f'Кнопка {j*3 + i}') for i in range(1, 4)] for j in range(3)]
keyboard_2 = ReplyKeyboardMarkup(
    keyboard=buttons_2,
    resize_keyboard=True
)


# keyboard_3
but_row_3: list[KeyboardButton] = [
    KeyboardButton(text=f'Кнопка {i}') for i in range(1, 10)
]
buttons_3: list[list[KeyboardButton]] = [
    [but_row_3[0]],
    but_row_3[1:3],
    but_row_3[3:6],
    but_row_3[6:8],
    [but_row_3[8]]
]
keyboard_3 = ReplyKeyboardMarkup(
    keyboard=buttons_3,
    resize_keyboard=True
)


# keyboard_4
buttons_4: list[list[KeyboardButton]] = [
    [KeyboardButton(text=f'{j*12 + i}') for i in range(1, 13)]
    for j in range(25)
]
keyboard_4 = ReplyKeyboardMarkup(
    keyboard=buttons_4,
    resize_keyboard=True
)


# keyboard_5
buttons_bld_1: list[KeyboardButton] = [
    KeyboardButton(text=f'Кнопка {i + 1}') for i in range(6)
]
buttons_bld_2: list[KeyboardButton] = [
    KeyboardButton(text=f'Кнопка {i + 7}') for i in range(4)
]
kb_builder_1 = ReplyKeyboardBuilder()
kb_builder_1.row(*buttons_bld_1, width=4)
kb_builder_1.row(*buttons_bld_2, width=3)
keyboard_5 = kb_builder_1.as_markup(
    resize_keyboard=True
)


# keyboard_6
buttons_bld_3: list[KeyboardButton] = [
    KeyboardButton(text=f'Кн. {i + 1}') for i in range(5)
]
buttons_bld_4: list[KeyboardButton] = [
    KeyboardButton(text=f'Кн. {i + 6}') for i in range(10)
]
kb_builder_2 = ReplyKeyboardBuilder()
kb_builder_2.row(*buttons_bld_3, width=4)
kb_builder_2.add(*buttons_bld_4)
kb_builder_2.adjust(2, 3, repeat=True)
keyboard_6 = kb_builder_2.as_markup(
    resize_keyboard=True
)


# keyboard_7
contact_btn = KeyboardButton(
    text='Отправить телефон',
    request_contact=True
)
geo_btn = KeyboardButton(
    text='Отправить геолокацию',
    request_location=True
)
poll_btn = KeyboardButton(
    text='Создать опрос',
    request_poll=KeyboardButtonPollType(type='regular')
)
quiz_btn = KeyboardButton(
    text='Создать викторину',
    request_poll=KeyboardButtonPollType(type='quiz')
)
web_app_btn = KeyboardButton(
    text='Start Web App',
    web_app=WebAppInfo(url='https://stepik.org/')
)
kb_builder_sp = ReplyKeyboardBuilder()
kb_builder_sp.row(contact_btn, geo_btn, poll_btn, quiz_btn,
                  web_app_btn, width=2)
keyboard_7 = kb_builder_sp.as_markup(
    resize_keyboard=True,
    one_time_keyboard=True
)
