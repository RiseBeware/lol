# === Stage 1: Создай базовую структуру файла приложения, точку входа и демонстрационные данные ===
# Project: TicketLedger
import json, uuid, datetime as dt
from dataclasses import dataclass, field, asdict
from typing import Optional, List

@dataclass
class Ticket:
    id: str = field(default_factory=lambda: str(uuid.uuid4())[:8])
    title: str = ""
    category: str = "General"
    priority: int = 3
    assignee: Optional[str] = None
    due_date: Optional[dt.datetime] = None
    status: str = "Open"
    resolution: Optional[str] = None

class TicketLedger:
    def __init__(self):
        self._tickets: List[Ticket] = []
    
    def add_ticket(self, title: str, category: str = "General", priority: int = 3) -> Ticket:
        t = Ticket(title=title, category=category, priority=priority)
        self._tickets.append(t)
        return t
    
    def list_tickets(self) -> List[dict]:
        return [asdict(t) for t in sorted(self._tickets, key=lambda x: (x.status != "Closed", -x.priority))]

if __name__ == "__main__":
    app = TicketLedger()
    app.add_ticket("Ошибка входа в систему", category="Security", priority=5)
    app.add_ticket("Добавить новую категорию", category="Feature", priority=2)
    print(json.dumps([asdict(t) for t in app._tickets], indent=2, default=str))
