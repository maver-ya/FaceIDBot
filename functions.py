import aiohttp
import telegram
import telegram.error
import asyncio
import logging

from aiogram import types
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import CallbackContext

from Messages import *
from db_func import *

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG
)

logger = logging.getLogger(__name__)


async def start(update: Update, context: CallbackContext):
    chat_id = update.message.chat_id
    await context.bot.send_message(text=start_text, chat_id=chat_id)
    keyboard = [
        [InlineKeyboardButton(text='Face ID', callback_data="face_id")],
        [InlineKeyboardButton(text='Пропуск', callback_data="let_pass")],
        [InlineKeyboardButton(text='Отмена', callback_data="cancel")]
    ]
    markup = InlineKeyboardMarkup(keyboard)
    await context.bot.send_message(text=what_way, chat_id=chat_id, reply_markup=markup)


async def button(update: Update, context: CallbackContext):
    if update.callback_query:
        query = update.callback_query
        await query.answer()
        context.user_data['query_data'] = query.data
        print(context.user_data['query_data'])
        if query.data == "face_id":
            await face_id(update, context)
    else:
        print(1)


async def face_id(update: Update, context: CallbackContext):
    await context.bot.send_message(text=get_name,
                                   chat_id=update.message.chat_id)

"""
@dp.message(F.text == "Отправить ФИО")
async def f_get_name(message: types.Message):
    user_id = message.from_user.id
    data = [*name.split(), user_id]
    print(data)
    if db_check(*data):
        kb = [
            [KeyboardButton(text="Обновим"),
             KeyboardButton(text="Оставим")]
        ]
        keyboard = ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True, input_field_placeholder="Выбери действие",
                                       one_time_keyboard=True)
        await message.answer("Вы уже есть в нашей базе!\nОбновим данные?",
                             reply_markup=keyboard)


@dp.message(F.text == "Обновим")
async def update_db(message: types.Message):
    data = get_data(message.from_user.id)
    await message.answer(data)
    kb = [
        [InlineKeyboardButton(text="Сохранить", callback_data="save")],
        [InlineKeyboardButton(text="Изменить", callback_data="change")],
        [InlineKeyboardButton(text="Удалить", callback_data="delete")]
    ]
    keyboard = InlineKeyboardMarkup(inline_keyboard=kb)
    await message.answer("Что Вы хотите сделать с Вашими данными?", reply_markup=keyboard)


@dp.message(F.text == "Оставим")
async def stay_db(message: types.Message):
    await cancel(message)


@dp.message(Command("cancel"))
async def cancel(message: types.Message):
    await message.answer("Ждем вас снова!")
"""