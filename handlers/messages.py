from aiogram import Router
from aiogram.filters import Text
from aiogram import types


router = Router()

# Хэндлер на сообщение "Далее".
@router.message(Text('Далее'))
async def msg_next(message: types.Message):
    await message.answer(
        text='SOME TEXT',
        reply_markup=types.ReplyKeyboardRemove(),
    )

# Хэндлер на сообщение "Выход".
@router.message(Text('Выход'))
async def msg_exit(message: types.Message):
    await message.answer(
        text='Пока-пока...',
        reply_markup=types.ReplyKeyboardRemove(),
    )