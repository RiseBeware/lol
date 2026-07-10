# === Stage 12: Добавь загрузку данных из локального JSON-файла с обработкой ошибок ===
# Project: TicketLedger
def load_tickets_from_json(file_path):
    """Загружает данные из локального JSON-файла с обработкой ошибок."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        if not isinstance(data, list):
            raise ValueError("JSON должен содержать массив записей")
        tickets = []
        for i, item in enumerate(data):
            try:
                ticket = {
                    'id': item.get('id', f'ticket_{i+1}'),
                    'title': item['title'],
                    'category': item.get('category', 'general'),
                    'priority': item.get('priority', 'medium'),
                    'assignee': item.get('assignee', None),
                    'deadline': item.get('deadline', None),
                    'status': item.get('status', 'open'),
                    'resolution': item.get('resolution', ''),
                }
                tickets.append(ticket)
            except KeyError as e:
                print(f"Предупреждение: пропущена запись {i+1} из-за отсутствия поля '{e}'")
        return tickets
    except FileNotFoundError:
        print(f"Ошибка: файл не найден — {file_path}")
        return []
    except json.JSONDecodeError as e:
        print(f"Ошибка: некорректный формат JSON — {e}")
        return []
