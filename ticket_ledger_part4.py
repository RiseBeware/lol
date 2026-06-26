# === Stage 4: Добавь функцию редактирования существующих записей по идентификатору ===
# Project: TicketLedger
def edit_ticket(ticket_id, updates):
    if ticket_id not in tickets:
        print(f"Заявка #{ticket_id} не найдена.")
        return False
    for key, value in updates.items():
        if hasattr(tickets[ticket_id], key) and value is not None:
            setattr(tickets[ticket_id], key, value)
    save_tickets()
    print(f"Заявка #{ticket_id} обновлена.")
    return True
