from aiogram import Router
from aiogram.filters import Command
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