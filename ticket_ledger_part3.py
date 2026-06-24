# === Stage 3: Реализуй хранение состояния в памяти и функции добавления записей ===
# Project: TicketLedger
class TicketLedger:
    def __init__(self):
        self._records = []
    
    def add_ticket(self, category, priority, assignee=None, due_date=None, status='open', description='', solution=None):
        record = {
            'id': len(self._records) + 1,
            'category': category,
            'priority': priority,
            'assignee': assignee,
            'due_date': due_date,
            'status': status,
            'description': description,
            'solution': solution
        }
        self._records.append(record)
        return record

    def get_all(self):
        return list(self._records)
