# === Stage 2: Добавь модели данных и функции валидации пользовательского ввода ===
# Project: TicketLedger
class Ticket:
    def __init__(self, title, description, category, priority, assignee=None, due_date=None):
        self.title = title.strip() or "Без названия"
        self.description = description.strip() if description else ""
        self.category = category.lower().strip() in ["bug", "feature", "question"] and category.lower().strip() or "other"
        self.priority = priority.lower().strip() in ["low", "medium", "high", "critical"] and priority.lower().strip() or "medium"
        self.assignee = assignee.strip() if assignee else None
        self.due_date = due_date

    def is_valid(self):
        return bool(self.title) and len(self.description) > 0
