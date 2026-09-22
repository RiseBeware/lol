# === Stage 46: Добавь миграцию версии структуры данных ===
# Project: TicketLedger
def migrate_v1():
    """Migration v1: adds resolution field to ticket structure."""
    if 'resolution' not in ticket_schema:
        ticket_schema['resolution'] = None
    print("Migration v1 complete: resolution field added.")
