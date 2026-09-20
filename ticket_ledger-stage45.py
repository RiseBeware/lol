# === Stage 45: Добавь восстановление из резервной копии ===
# Project: TicketLedger
import json, os

def load_from_backup(backup_path):
    if not os.path.exists(backup_path):
        raise FileNotFoundError(f"Резервная копия не найдена: {backup_path}")
    with open(backup_path, "r", encoding="utf-8") as f:
        return json.load(f)

def save_to_backup(data, backup_path):
    os.makedirs(os.path.dirname(backup_path) or ".", exist_ok=True)
    with open(backup_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def migrate_legacy(legacy_path, new_path):
    if os.path.exists(legacy_path):
        with open(legacy_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        save_to_backup(data, new_path)
        return True
    return False
