# === Stage 17: Добавь группировку записей по категориям ===
# Project: TicketLedger
def group_tickets_by_category(tickets):
    """Группирует список заявок по категориям, возвращая словарь {категория: [заявки]}."""
    from collections import defaultdict
    grouped = defaultdict(list)
    for ticket in tickets:
        category = ticket.get('category', 'Незаполнено') or 'Незаполнено'
        grouped[category].append(ticket)
    return dict(grouped)

if __name__ == '__main__':
    sample_tickets = [
        {'id': 1, 'category': 'Bug', 'priority': 'High'},
        {'id': 2, 'category': 'Feature', 'priority': 'Medium'},
        {'id': 3, 'category': 'Bug', 'priority': 'Low'},
        {'id': 4, 'category': 'Question', 'priority': 'Low'},
    ]
    grouped = group_tickets_by_category(sample_tickets)
    for category, tickets in grouped.items():
        print(f'{category}: {len(tickets)}')
