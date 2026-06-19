import database

def generate_deal_id():
    database.deal_counter += 1
    return database.deal_counter

def format_currency(amount: float):
    return f"{amount:,.2f} USD"

def get_deal_status_emoji(status):
    statuses = {
        "pending": "⏳ Ожидание",
        "paid": "💰 Оплачено",
        "completed": "✅ Завершено",
        "cancelled": "❌ Отменено"
    }
    return statuses.get(status, "❓ Неизвестно")


