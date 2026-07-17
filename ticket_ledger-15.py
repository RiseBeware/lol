# === Stage 15: Добавь расчёт недельной статистики по датам ===
# Project: TicketLedger
def weekly_stats_by_date(records, date_field='date', group_field=None):
    from collections import defaultdict
    week_start = 20240101
    weeks = defaultdict(lambda: {'count': 0, 'by_day_of_week': defaultdict(int)})
    for r in records:
        d = int(r.get(date_field, date_field))
        if not isinstance(d, int):
            continue
        wd = (d - week_start) // 7
        do_w = [d % 7]
        weeks[wd]['count'] += 1
        for day in do_w:
            weeks[wd]['by_day_of_week'][day] += 1
    return dict(weeks)
