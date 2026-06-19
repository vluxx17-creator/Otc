from typing import Callable, Dict, Any, Awaitable
from aiogram import BaseMiddleware
from aiogram.types import TelegramObject, Message

ADMIN_IDS = [123456789] # Список ID администраторов

class AdminMiddleware(BaseMiddleware):
    async def __call__(
        self, 
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]], 
        event: TelegramObject, 
        data: Dict[str, Any]
    ) -> Any:
        # Проверяем, является ли пользователь админом
        if isinstance(event, (Message, CallbackQuery)) and event.from_user.id in ADMIN_IDS:
            return await handler(event, data)
        
        # Если не админ
        if isinstance(event, CallbackQuery):
            await event.answer("У вас нет прав администратора!", show_alert=True)
        return # Блокируем выполнение
