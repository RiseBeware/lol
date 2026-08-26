# === Stage 29: Добавь конфигурацию приложения через словарь настроек ===
# Project: TicketLedger
CONFIG = {
    "app_name": "TicketLedger",
    "version": "0.1.0",
    "db_file": "tickets.db",
    "max_priority": 5,
    "priority_labels": {1: "Низкий", 2: "Нормальный", 3: "Высокий", 4: "Критический", 5: "Экстренный"},
    "allowed_categories": ["Техническая", "Организационная", "Питание", "Другое"],
    "default_assignee": None,
    "log_level": "INFO",
    "allowed_log_levels": {"DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"},
    "session_timeout": 3600,
}
