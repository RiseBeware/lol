# === Stage 8: Реализуй текстовый интерфейс команд с меню действий ===
# Project: TicketLedger
def run_cli():
    menu = ["1. Создать заявку", "2. Просмотреть список", "3. Изменить статус", "4. Выйти"]
    while True:
        print("\n=== TicketLedger CLI ===")
        for i, item in enumerate(menu):
            print(f"{i+1}. {item}")
        try:
            choice = input("Выберите действие (или 'q' для выхода): ").strip()
            if choice.lower() == "q":
                break
            elif choice.isdigit():
                idx = int(choice) - 1
                if idx < len(menu):
                    print(f"Вы выбрали: {menu[idx]}")
                    # Здесь можно добавить логику вызова соответствующих функций проекта
                    # Например: create_ticket() или list_tickets()
                    input("Нажмите Enter, чтобы продолжить...")
            else:
                print("Неверный ввод.")
        except KeyboardInterrupt:
            print("\nВыход из программы.")
            break
