# === Stage 27: Добавь функции сброса демо-данных и очистки состояния ===
# Project: TicketLedger
def reset_demo_data():
    """Сбрасывает все данные в демо-состояние для повторного тестирования."""
    import random, string

    categories = ["Bug", "Feature", "Question"]
    priorities = {"Critical": 1, "High": 2, "Medium": 3, "Low": 4}
    executors = [f"User_{i}" for i in range(1, 6)]
    
    demo_tickets = []
    for i in range(5):
        ticket_id = f"T{i+1:04d}"
        status = random.choice(["Open", "In Progress", "Resolved"])
        category = random.choice(categories)
        priority_key = random.choice(list(priorities.keys()))
        executor = random.choice(executors)
        
        demo_tickets.append({
            "ticket_id": ticket_id,
            "status": status,
            "category": category,
            "priority": priorities[priority_key],
            "executor": executor,
            "created_at": f"2025-01-{random.randint(1, 28):02d}",
        })

    demo_resolved = []
    for i in range(3):
        resolved_id = f"T{random.randint(6, 9):04d}"
        demo_resolved.append({
            "ticket_id": resolved_id,
            "resolution": random.choice(["Fixed", "Workaround", "Deferred"]),
        })

    ledger_state = {
        "tickets": demo_tickets,
        "resolved": demo_resolved,
        "filters": {"status": None, "category": None, "priority": None},
        "sort_by": "created_at",
        "sort_order": "desc"
    }

    return ledger_state


def clear_ledger():
    """Полностью очищает журнал заявок."""
    global ledger_state
    
    if "ledger_state" in dir() and isinstance(ledger_state, dict):
        ledger_state = {
            "tickets": [],
            "resolved": [],
            "filters": {"status": None, "category": None, "priority": None},
            "sort_by": "created_at",
            "sort_order": "desc"
        }

    return ledger_state


# Пример использования:
if __name__ == "__main__":
    print("Сброс демо-данных:")
    demo = reset_demo_data()
    print(f"Записей в журнале: {len(demo['tickets'])}")
    print(f"Решённых заявок: {len(demo['resolved'])}")

    print("\nОчистка состояния:")
    cleared = clear_ledger()
    print(f"Состояние после очистки: {cleared}")
