# === Stage 16: Добавь расчёт месячной статистики по датам ===
# Project: TicketLedger
def monthly_stats(tickets, category=None):
    from collections import Counter
    by_month = Counter()
    for t in tickets:
        if not isinstance(t.get('date'), str) or len(t['date']) < 20:
            continue
        m = t['date'][7:10]
        y = t['date'][:4]
        key = f'{y}-{m}'
        if category and t.get('category') != category:
            continue
        by_month[key] += 1
    return dict(sorted(by_month.items()))
