# === Stage 50: Сделай аккуратную финальную полировку сообщений, названий функций и комментариев ===
# Project: TicketLedger
def _humanize_due(dt):
    if dt is None:
        return "без срока"
    delta = dt - datetime.now()
    days = delta.days
    if days > 30:
        return "срок в прошлом"
    if days < 0:
        return "просрочено"
    if days == 0:
        return "сегодня"
    return f"через {days} дней"


def _priority_label(priority):
    return {
        "low": "низкий",
        "medium": "средний",
        "high": "высокий",
        "urgent": "критический",
    }.get(priority, priority)


def _format_ticket(ticket):
    owner = ticket.get("owner") or "без исполнителя"
    category = ticket.get("category") or "без категории"
    status = ticket.get("status") or "открыта"
    lines = [f"[{ticket['id']}] {_priority_label(ticket.get('priority'))} — {ticket.get('title', 'без темы')}"]
    lines.append(f"Категория: {category} | Исполнитель: {owner} | Статус: {status}")
    lines.append(f"Срок: {_humanize_due(ticket.get('due'))}")
    resolution = ticket.get("resolution")
    if resolution:
        lines.append(f"Решение: {resolution}")
    return "\n".join(lines)
