# === Stage 10: Добавь экспорт текущего состояния в JSON-строку ===
# Project: TicketLedger
def export_to_json(tickets: list, categories: dict, priorities: dict, assignees: dict) -> str:
    """Export the full ticket ledger state to a single JSON string."""
    import json

    def serialize(obj):
        if isinstance(obj, (str, int, float, bool, type(None))):
            return obj
        if isinstance(obj, list):
            return [serialize(item) for item in obj]
        if isinstance(obj, dict):
            return {k: serialize(v) for k, v in obj.items()}
        return str(obj)

    data = {
        "categories": categories,
        "priorities": priorities,
        "assignees": assignees,
        "tickets": [serialize(t) for t in tickets]
    }
    return json.dumps(data, ensure_ascii=False, indent=2)
