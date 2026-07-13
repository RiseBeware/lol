# === Stage 13: Добавь поиск по нескольким полям без учёта регистра ===
# Project: TicketLedger
def search_tickets(query: str, tickets: list) -> list:
    query = query.lower().strip()
    if not query:
        return tickets
    results = []
    for t in tickets:
        searchable = (t.get('title', '') + ' ' + t.get('description', '') + ' ' + t.get('category', '') + ' ' + t.get('status', '')).lower()
        if query in searchable:
            results.append(t)
    return results
