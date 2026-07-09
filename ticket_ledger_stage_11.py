# === Stage 11: Добавь сохранение данных в локальный JSON-файл ===
# Project: TicketLedger
import json


def load_tickets(path="tickets.json"):
    if not path.exists():
        return []
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data.get("tickets", [])


def save_tickets(tickets, path="tickets.json"):
    with open(path, "w", encoding="utf-8") as f:
        json.dump({"tickets": tickets}, f, ensure_ascii=False, indent=2)
