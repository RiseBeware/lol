# === Stage 7: Добавь сортировку записей по дате, приоритету и названию ===
# Project: TicketLedger
def sort_tickets(tickets, key='date'):
    if key == 'priority':
        priority_map = {'critical': 0, 'high': 1, 'medium': 2, 'low': 3}
        return sorted(tickets, key=lambda t: (priority_map.get(t['priority'], 4), t['name']))
    elif key == 'name':
        return sorted(tickets, key=lambda t: t['name'])
    else:
        return sorted(tickets, key=lambda t: t['date'])
