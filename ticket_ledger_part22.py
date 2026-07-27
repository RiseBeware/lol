# === Stage 22: Добавь проверку просроченных напоминаний ===
# Project: TicketLedger
def check_overdue_reminders(tickets, now=None):
    if now is None:
        import datetime
        now = datetime.datetime.utcnow()
    overdue = []
    for t in tickets:
        deadline = t.get('deadline')
        assigned_at = t.get('assigned_at')
        if not assigned_at or not deadline:
            continue
        try:
            dl_dt = datetime.datetime.fromtimestamp(deadline)
            assign_dt = datetime.datetime.fromtimestamp(assigned_at)
            delta = now - assign_dt
            threshold = timedelta(days=2)
            if delta > threshold and now > dl_dt:
                overdue.append({
                    'ticket_id': t['id'],
                    'title': t.get('title', ''),
                    'deadline': dl_dt,
                    'remaining_hours': round((dl_dt - now).total_seconds() / 3600, 2),
                    'status': t.get('status'),
                })
        except (ValueError, OSError):
            continue
    return overdue
