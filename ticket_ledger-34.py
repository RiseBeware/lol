# === Stage 34: Добавь простую систему шаблонов для быстрого создания записей ===
# Project: TicketLedger
TEMPLATE_REGISTRY = {}

class Template:
    def __init__(self, name, category=None, priority=None, assignee=None, due=None, status=None, description=None):
        self.name = name
        self.category = category
        self.priority = priority
        self.assignee = assignee
        self.due = due
        self.status = status
        self.description = description

    def apply(self, ticket, ledger):
        if self.category:
            ticket.category = self.category
        if self.priority:
            ticket.priority = self.priority
        if self.assignee:
            ticket.assignee = self.assignee
        if self.due:
            ticket.due = self.due
        if self.status:
            ticket.status = self.status
        if self.description:
            ticket.description = self.description
        return ticket

def register_template(name, template):
    TEMPLATE_REGISTRY[name] = template

def create_from_template(template_name, ledger):
    template = TEMPLATE_REGISTRY.get(template_name)
    if not template:
        print(f"Template '{template_name}' not found.")
        return None
    ticket = Ticket()
    template.apply(ticket, ledger)
    return ticket
