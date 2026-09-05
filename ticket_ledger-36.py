# === Stage 36: Добавь проверку целостности данных и функцию ремонта простых проблем ===
# Project: TicketLedger
def repair_ticket(ticket):
    """Функция ремонта: исправляет типичные проблемы, например, пустые поля и некорректные приоритеты."""
    if not ticket.get("priority") or ticket["priority"].lower() not in ["low", "medium", "high", "critical"]:
        ticket["priority"] = "medium"
    if not ticket.get("status") or ticket["status"].lower() not in ["open", "in_progress", "resolved", "closed"]:
        ticket["status"] = "open"
    if not ticket.get("assignee"):
        ticket["assignee"] = None
    if not ticket.get("resolution") and ticket["status"] == "resolved":
        ticket["resolution"] = "no resolution provided"
    return ticket
