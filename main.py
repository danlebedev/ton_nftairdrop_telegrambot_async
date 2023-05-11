import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

import config
from handlers import all_handlers


# Запуск бота.
async def main():
    # Включаем логирование, чтобы не пропустить важные сообщения.
    logging.basicConfig(level=logging.INFO)
    # Объект бота.
    bot = Bot(token=config.token)
    # Диспетчер.
    dp = Dispatcher(storage=MemoryStorage())
    # Добавляем роутеры.
    dp.include_routers(
        all_handlers.router,
    )

    # Запускаем бота и пропускаем все накопленные входящие.
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())