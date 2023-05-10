from aiogram import Router
from aiogram.filters import Command
from aiogram import types

router = Router()

# Хэндлер на команду /start
@router.message(Command('start'))
async def cmd_start(message: types.Message):
    await message.answer('Hello!')