# === Stage 21: Добавь простую систему напоминаний с датой выполнения ===
# Project: TicketLedger
def notify_upcoming_tickets():
    """Print tickets whose deadline is within the next 3 days."""
    now = datetime.now()
    for t in ticket_ledger:
        if t.deadline and (t.deadline - now).days <= 3:
            print(f"⏰ {t.title} — срок: {t.deadline.strftime('%d.%m')}, ответственный: {t.assigned}")

notify_upcoming_tickets()
