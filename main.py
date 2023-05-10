import asyncio
import logging
from aiogram import Bot, Dispatcher

import config
from handlers import commands


# Запуск бота.
async def main():
    # Включаем логирование, чтобы не пропустить важные сообщения.
    logging.basicConfig(level=logging.INFO)
    # Объект бота.
    bot = Bot(token=config.token)
    # Диспетчер.
    dp = Dispatcher()
    # Добавляем роутеры.
    dp.include_routers(
        commands.router,
    )

    # Запускаем бота и пропускаем все накопленные входящие.
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())