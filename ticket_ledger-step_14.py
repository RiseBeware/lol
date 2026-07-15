# === Stage 14: Добавь генерацию краткой сводки по текущим данным ===
# Project: TicketLedger
def summary_report(tickets, categories=None):
    if not tickets:
        return f"📋 Нет заявок.\n\n{len(tickets)} всего | 0 открытых | 0 закрытых"
    
    total = len(tickets)
    open_count = sum(1 for t in tickets if t['status'] == 'open')
    closed_count = total - open_count
    
    overdue = sum(1 for t in tickets if t['due_date'] and datetime.date.today() > datetime.date.fromisoformat(t['due_date']) and t['status'] == 'open')
    
    cat_dist = {}
    for t in tickets:
        c = t.get('category', 'Не задан')
        cat_dist[c] = cat_dist.get(c, 0) + 1
    
    priority_dist = {}
    for t in tickets:
        p = t['priority']
        priority_dist[p] = priority_dist.get(p, 0) + 1
    
    executors = set(t['executor'] for t in tickets if t['status'] == 'open')
    
    lines = [f"📊 Сводка по заявкам ({total})"]
    lines.append(f"  Открыто: {open_count} | Закрыто: {closed_count}")
    if overdue > 0:
        lines.append(f"  ⚠️ Пропущены сроки: {overdue}")
    
    for p, cnt in sorted(priority_dist.items(), key=lambda x: {"high": 0, "medium": 1, "low": 2}.get(x[0], 3)):
        if cnt > 0:
            lines.append(f"  Приоритет {p}: {cnt}")
    
    for c, cnt in sorted(cat_dist.items(), key=lambda x: -x[1]):
        if cnt > 0:
            lines.append(f"  Категория {c}: {cnt}")
    
    executors_str = ", ".join(executors) if executors else "Нет активных исполнителей"
    lines.append(f"  Исполнители: {executors_str}")
    
    return "\n".join(lines)
