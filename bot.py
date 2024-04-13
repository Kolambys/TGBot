import asyncio
from aiogram import Bot, Dispatcher
import other_handlers, user_handlers




async def main():
    TOKEN = '5112423873:AAEaUlfCejM41d0cfLzuIW50ywZmAu6zX2Q'


    bot = Bot(token=TOKEN, parse_mode='HTML')
    dp = Dispatcher()


    dp.include_router(user_handlers.router)
    dp.include_router(other_handlers.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
