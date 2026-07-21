# === Stage 18: Добавь поддержку тегов и операции добавления/удаления тегов ===
# Project: TicketLedger
class TicketTag:
    def __init__(self, name):
        self.name = name.lower()

    def __repr__(self):
        return f'TicketTag("{self.name}")'


def add_tag(ticket_id, tag_name):
    ticket = get_ticket(ticket_id)
    if not ticket:
        print(f"Ticket {ticket_id} не найден")
        return None
    tags = ticket.get('tags', [])
    existing = [t for t in tags if t.lower() == tag_name]
    if existing:
        return ticket  # уже есть, ничего не меняем
    tags.append(tag_name)
    set_field(ticket_id, 'tags', tags)
    return ticket


def remove_tag(ticket_id, tag_name):
    ticket = get_ticket(ticket_id)
    if not ticket:
        print(f"Ticket {ticket_id} не найден")
        return None
    tags = ticket.get('tags', [])
    new_tags = [t for t in tags if t.lower() != tag_name]
    if len(new_tags) == len(tags):
        return ticket  # тег удалён, но ничего не изменилось
    set_field(ticket_id, 'tags', new_tags)
    return ticket
