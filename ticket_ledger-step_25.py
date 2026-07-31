# === Stage 25: Добавь обработку некорректных дат и понятные сообщения об ошибках ===
# Project: TicketLedger
def parse_date(date_str):
    """Парсит дату из строки, возвращает datetime или сообщение об ошибке."""
    try:
        from datetime import datetime
        formats = [
            "%Y-%m-%d",
            "%d.%m.%Y",
            "%d %B %Y",
            "%d %b %Y",
        ]
        for fmt in formats:
            try:
                return datetime.strptime(date_str.strip(), fmt)
            except ValueError:
                continue
        raise ValueError(f"Некорректный формат даты: '{date_str}'")
    except (ValueError, TypeError) as e:
        return f"Ошибка: {e}"

def parse_date_safe(date_str):
    """Парсит дату, возвращает datetime или None при ошибке."""
    try:
        from datetime import datetime
        formats = [
            "%Y-%m-%d",
            "%d.%m.%Y",
            "%d %B %Y",
            "%d %b %Y",
        ]
        for fmt in formats:
            try:
                return datetime.strptime(date_str.strip(), fmt)
            except ValueError:
                continue
        return None
    except Exception:
        return None
