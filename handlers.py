from aiogram import Router, F
from aiogram.types import CallbackQuery
import database
import utils
import keyboards

router = Router()

@router.callback_query(F.data.startswith("finish_deal_"))
async def finish_deal(callback: CallbackQuery):
    deal_id = int(callback.data.split("_")[2])
    
    if deal_id not in database.deals:
        return await callback.answer("Сделка не найдена!")

    # Логика завершения
    database.deals[deal_id]["status"] = "completed"
    
    # Используем утилиту для красоты
    amount_str = utils.format_currency(database.deals[deal_id]["amount"])
    
    await callback.message.edit_text(
        f"Сделка #{deal_id} успешно завершена!\n"
        f"Сумма {amount_str} переведена продавцу."
    )


