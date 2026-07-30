# === Stage 24: Добавь компактный вывод одной записи с деталями ===
# Project: TicketLedger
def show_ticket(self, ticket):
        print(f"ID: {ticket['id']}")
        print(f"Subject: {ticket['subject']}")
        print(f"Status: {ticket.get('status', 'N/A')}")
        print(f"Priority: {ticket.get('priority', 'N/A')}")
        print(f"Category: {ticket.get('category', 'N/A')}")
        if ticket.get('assignee'):
            print(f"Assignee: {ticket['assignee']}")
        else:
            print("Assignee: None")
        due = ticket.get('due_date')
        created = ticket.get('created_at')
        if due and isinstance(due, datetime):
            delta = (datetime.now() - due).total_seconds() / 3600
            if delta < 0:
                print(f"Due: {delta:.1f}h ago")
            else:
                print(f"Due: +{delta:.1f}h")
        elif isinstance(due, str):
            print(f"Due: {due}")
        else:
            print("Due: N/A")
        if ticket.get('resolution'):
            print(f"Resolution: {ticket['resolution']}")
        print("---")


if __name__ == "__main__":
    ledger = TicketLedger()
    ledger.add_ticket({"id": "T-001", "subject": "Server down", "status": "open", "priority": "high", "category": "infrastructure", "assignee": "Admin", "created_at": datetime.now(), "due_date": datetime.now() + timedelta(hours=2)})
    ledger.add_ticket({"id": "T-002", "subject": "New feature request", "status": "pending", "priority": "medium", "category": "feature"})
    print("=== Ticket Ledger ===")
    for t in ledger.tickets:
        ledger.show_ticket(t)
