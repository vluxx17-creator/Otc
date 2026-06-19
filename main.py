import asyncio
from aiogram import Bot, Dispatcher
from handlers import router as main_router
# Импортируйте здесь middleware, если он будет

# Вставьте ваш токен
API_TOKEN = "ВАШ_ТОКЕН_ОТ_BOTFATHER"

async def main():
    bot = Bot(token=API_TOKEN)
    dp = Dispatcher()
    
    # Регистрация роутеров
    dp.include_router(main_router)
    
    print("Бот запущен...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Бот выключен")
