# === Stage 47: Добавь финальную функцию demo(), которая показывает основной пользовательский сценарий ===
# Project: TicketLedger
def demo():
    from datetime import datetime
    print("=== TicketLedger Demo ===\n")
    cat = Category("Bug", "баги")
    pri = Priority("High", "критичный")
    user = User("Alice", "alice@example.com", "backend")
    ticket = Ticket("AUTH-001", "Login fails on mobile", cat, pri, user,
                    due=datetime(2026, 1, 15), resolved=datetime(2026, 1, 10),
                    solution="Fixed JWT expiry logic")
    ticket.status = "resolved"
    ticket.comments.append("Initial report")
    ticket.comments.append("Reproduced on device X")
    ticket.comments.append("Solution verified")
    ticket.comments.append("Ready for release")
    ticket.comments.append("Closed by QA")
    journal = Journal()
    journal.add(ticket)
    print(f"Ticket #{ticket.id}: {ticket}")
    print(f"Comments ({len(ticket.comments)}):")
    for c in ticket.comments:
        print(f"  - {c}")
    print(f"\nAll tickets: {journal}")
    print("Demo finished.")
