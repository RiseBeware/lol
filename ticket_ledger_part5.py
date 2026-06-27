# === Stage 5: Добавь удаление записей и аккуратную обработку отсутствующих идентификаторов ===
# Project: TicketLedger
def delete_ticket(ticket_id: int) -> bool:
    if ticket_id not in tickets_db:
        print(f"Ошибка: запись с ID {ticket_id} не найдена.")
        return False
    
    deleted = tickets_db.pop(ticket_id, None)
    if deleted is None:
        print(f"Ошибка: удаление записи с ID {ticket_id} не удалось (возможно, она была удалена ранее).")
        return False
        
    print(f"Успешно удалена заявка #{deleted['id']}: {deleted.get('title', 'Без названия')} ({deleted.get('category', 'Неизвестная')})")
    return True

def handle_missing_id(ticket_id: int) -> None:
    if ticket_id not in tickets_db:
        print(f"Предупреждение: попытка работы с несуществующей заявкой ID={ticket_id}. Проверьте корректность идентификатора.")
