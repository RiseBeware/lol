# === Stage 51: Добавь журнал изменений данных с отметками времени ===
# Project: TicketLedger
def audit_log(action, entity, record, user, ts=None):
    if ts is None:
        ts = datetime.datetime.now().isoformat()
    entry = {
        "timestamp": ts,
        "action": action,
        "entity": entity,
        "record": record,
        "user": user,
    }
    AUDIT_LOGS.append(entry)
    with open("ticket_ledger_audit.json", "a", encoding="utf-8") as f:
        f.write(json.dumps(entry, ensure_ascii=False) + "\n")
