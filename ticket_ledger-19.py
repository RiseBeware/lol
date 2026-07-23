# === Stage 19: Добавь функцию архивации завершённых или старых записей ===
# Project: TicketLedger
import datetime

MAX_ARCHIVE_AGE = datetime.timedelta(days=30)

def archive_old_tickets(tickets: list[dict]) -> tuple[list[dict], list[dict]]:
    """Returns (archived, remaining)."""
    now = datetime.datetime.now()
    archived = []
    for t in tickets:
        created = datetime.datetime.fromisoformat(t.get("created_at", ""))
        if now - created > MAX_ARCHIVE_AGE or t.get("status") == "closed":
            t["archived"] = True
            archived.append(t)
        else:
            t["archived"] = False
    return archived, tickets[len(archived):]
