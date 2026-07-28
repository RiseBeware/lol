# === Stage 23: Добавь форматированный вывод таблицей в консоль ===
# Project: TicketLedger
def print_ticket_table(tickets):
    if not tickets:
        print("Список заявок пуст.")
        return
    headers = ["ID", "Категория", "Приоритет", "Исполнитель", "Дедлайн", "Статус"]
    widths = [len(h) for h in headers]
    for t in tickets:
        row = []
        for h in headers:
            val = getattr(t, h.replace(" ", "_"), "")
            w = max(widths[0], len(str(val))) if h == "ID" else 12
            widths.append(w)
