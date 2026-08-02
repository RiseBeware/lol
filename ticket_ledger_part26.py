# === Stage 26: Добавь набор демо-команд для быстрого ручного тестирования ===
# Project: TicketLedger
def demo():
    print("=== TicketLedger Demo ===")
    for ticket in tickets:
        status = "Resolved" if ticket.resolution else "Open"
        priority_emoji = {"Critical": "🔴", "High": "🟠", "Medium": "🟡", "Low": "🟢"}.get(ticket.priority, "?")
        print(f"{priority_emoji} [{ticket.id}] {ticket.title}")
        if ticket.assignee:
            print(f"    Assigned to: {ticket.assignee.name}")
        else:
            print(f"    Status: {status}")
        print()

if __name__ == "__main__":
    demo()
