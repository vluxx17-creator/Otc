import os
from dotenv import load_dotenv

# Загружаем переменные из .env
load_dotenv()

# Получаем данные
BOT_TOKEN = os.getenv("BOT_TOKEN")

# Преобразуем строку "123,456" в список целых чисел [123, 456]
raw_admin_ids = os.getenv("ADMIN_IDS", "")
ADMIN_IDS = [int(id.strip()) for id in raw_admin_ids.split(",") if id.strip().isdigit()]

# Проверка, что токен вообще был загружен
if not BOT_TOKEN:
    raise ValueError("Ошибка: BOT_TOKEN не найден в .env файле!")


