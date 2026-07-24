# === Stage 20: Добавь восстановление записей из архива ===
# Project: TicketLedger
def archive_recovery(tickets, recovery_id=None):
    """Restore all archived tickets back into the active list."""
    if recovery_id is not None:
        return [t for t in tickets if t.get('status') == 'archived' and t.get('id') == recovery_id]
    return [t for t in tickets if t.get('status') == 'archived']

def restore_to_active(tickets, to_restore):
    """Mark restored ticket IDs as active again."""
    for t in tickets:
        if t.get('id') in to_restore:
            t['status'] = 'active'
