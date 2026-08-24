# === Stage 28: Добавь подсчёт ключевых метрик проекта ===
# Project: TicketLedger
def print_project_metrics(tickets: list[dict]) -> None:
    if not tickets:
        print("Нет данных для анализа.")
        return
    total = len(tickets)
    closed = sum(1 for t in tickets if t.get("status") == "closed")
    open_count = total - closed
    avg_days = (
        sum((t.get("resolved_at") or t.get("due_date") or 0) - (t.get("created_at") or 0) for t in tickets)
        / total
        if total
        else 0
    )
    print(f"Всего заявок: {total} | Закрыто: {closed} | Открыто: {open_count} | Среднее время: {avg_days:.1f} дней")
