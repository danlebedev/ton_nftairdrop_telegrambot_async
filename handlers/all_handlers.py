from aiogram import Router
from aiogram.filters import Command, Text
from aiogram import types
from aiogram.utils.keyboard import ReplyKeyboardBuilder


router = Router()

# Хэндлер на команду /start.
@router.message(Command('start'))
async def cmd_start(message: types.Message):
    builder = ReplyKeyboardBuilder()
    builder.add(types.KeyboardButton(text='Далее'))
    builder.add(types.KeyboardButton(text='Выход'))
    await message.answer(
        text='Hello!',
        reply_markup=builder.as_markup(resize_keyboard=True),
    )

# Хэндлер на сообщение "Далее".
@router.message(Text('Далее'))
async def msg_next(message: types.Message):
    await message.answer(
        text='SOME TEXT',
        reply_markup=types.ReplyKeyboardRemove(),
    )

# Хэндлеры на сообщение "Выход" и команду /stop.
@router.message(Text('Выход'))
@router.message(Command('stop'))
async def msg_exit(message: types.Message):
    await message.answer(
        text='Пока-пока...',
        reply_markup=types.ReplyKeyboardRemove(),
    )