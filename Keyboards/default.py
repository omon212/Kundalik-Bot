from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

button = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="O'quvchi 👨‍🎓"),
            KeyboardButton(text="O'qituvchi 👨🏻‍🏫")
        ],
    ],
    resize_keyboard=True
)
contact = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Contact", request_contact=True),
        ]
    ],
    resize_keyboard=True
)
