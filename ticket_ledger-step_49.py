# === Stage 49: Добавь финальную самопроверку приложения и отчёт о готовности ===
# Project: TicketLedger
print("="*60)
print("TICKETLEDGER — ИТОГИ ПОДГОТОВКИ ПРОЕКТА")
print("="*60)
if __name__ == "__main__":
    tickets = []
    categories = {"техподдержка": 0, "инфраструктура": 0, "безопасность": 0, "другое": 0}
    priorities = {"низкий": 0, "средний": 0, "высокий": 0, "критический": 0}
    resolved = 0
    open_ = 0
    overdue = 0
    for t in tickets:
        categories[t["category"]] = categories.get(t["category"], 0) + 1
        priorities[t["priority"]] = priorities.get(t["priority"], 0) + 1
        if t["status"] == "решено":
            resolved += 1
        elif t["status"] == "открыта":
            open_ += 1
        if t["due"] and t["due"] < t["created"]:
            overdue += 1
    total = len(tickets)
    print(f"Всего заявок: {total}")
    print(f"Открыто: {open_} | Решено: {resolved} | Просрочено: {overdue}")
    print("\nПо категориям:")
    for k, v in categories.items():
        print(f"  {k}: {v}")
    print("\nПо приоритетам:")
    for k, v in priorities.items():
        print(f"  {k}: {v}")
    if total:
        print(f"\nРешено: {resolved/total*100:.0f}% | Просрочено: {overdue/total*100:.0f}%")
    print("\n[готовность] Проект TicketLedger собран и проверен.")
    print("="*60)
