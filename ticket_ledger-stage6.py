# === Stage 6: Добавь фильтрацию записей по статусу, категории или тегам ===
# Project: TicketLedger
def filter_tickets(status=None, category=None, tags=None):
    filtered = []
    for ticket in tickets:
        if status and ticket['status'] != status:
            continue
        if category and ticket.get('category') != category:
            continue
        if tags:
            ticket_tags = set(ticket.get('tags', [])).intersection(set(tags))
            if not ticket_tags:
                continue
        filtered.append(ticket)
    return filtered
