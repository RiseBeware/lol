# === Stage 48: Проведи рефакторинг: разнеси крупные функции, сохрани совместимость публичных команд ===
# Project: TicketLedger
import re

PRIORITY_ORDER = {"low": 0, "medium": 1, "high": 2, "urgent": 3}

def _split_ticket_line(line):
    fields = line.split("|")
    if len(fields) < 6:
        return None
    return {
        "id": fields[0].strip(),
        "subject": fields[1].strip(),
        "category": fields[2].strip(),
        "priority": fields[3].strip().lower(),
        "assignee": fields[4].strip(),
        "due": fields[5].strip(),
        "status": fields[6].strip() if len(fields) > 6 else "open",
    }

def _validate_ticket(ticket):
    if not ticket["id"] or not ticket["subject"]:
        return "ID и тема обязательны"
    if ticket["priority"] not in PRIORITY_ORDER:
        return "Неверный приоритет"
    return None

def _sort_tickets(tickets):
    return sorted(
        tickets,
        key=lambda t: (
            PRIORITY_ORDER.get(t["priority"], 0),
            t["due"],
            t["id"],
        ),
    )

def _format_ticket_row(ticket):
    return (
        f'{ticket["id"]} | {ticket["subject"]} | {ticket["category"]} | '
        f'{ticket["priority"].upper()} | {ticket["assignee"]} | {ticket["due"]} | '
        f'{ticket["status"]}'
    )

def _render_journal(tickets):
    lines = []
    lines.append(f"{'ID':<4} | {'Тема':<20} | {'Категория':<12} | "
                 f"{'Приоритет':<8} | {'Исполнитель':<12} | {'Срок':<12} | {'Статус'}")
    lines.append("-" * 90)
    for ticket in tickets:
        lines.append(_format_ticket_row(ticket))
    return "\n".join(lines)
