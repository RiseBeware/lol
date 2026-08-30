# === Stage 32: Добавь журнал действий пользователя ===
# Project: TicketLedger
class ActionLog:
    def __init__(self, ledger):
        self.ledger = ledger
        self.actions = []

    def log(self, user, action, details=None):
        record = {"user": user, "action": action, "timestamp": datetime.now().isoformat(), "details": details}
        self.actions.append(record)
        if details:
            self.ledger.print_action_log()
        return record

    def print_action_log(self):
        if not self.actions:
            print("Действий не записано.")
        else:
            print("=== Журнал действий ===")
            for i, rec in enumerate(self.actions, 1):
                print(f"{i}. {rec['user']} — {rec['action']} [{rec['timestamp']}]")
                if rec["details"]:
                    print(f"   Детали: {rec['details']}")
