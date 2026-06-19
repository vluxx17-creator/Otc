from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def main_menu():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Создать сделку", callback_data="create_deal")],
        [InlineKeyboardButton(text="Мои сделки", callback_data="my_deals")],
        [InlineKeyboardButton(text="Админка", callback_data="admin_panel")]
    ])

def admin_deal_kb(deal_id):
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="✅ Завершить и выдать деньги", callback_data=f"finish_deal_{deal_id}")],
        [InlineKeyboardButton(text="❌ Отменить", callback_data=f"cancel_deal_{deal_id}")]
    ])


