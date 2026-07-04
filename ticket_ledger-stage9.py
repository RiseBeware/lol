# === Stage 9: Добавь импорт начальных данных из JSON-строки ===
# Project: TicketLedger
import json, os, sys

def load_initial_data(json_string):
    try:
        data = json.loads(json_string)
        if not isinstance(data, dict):
            raise ValueError("JSON должен содержать объект")
        
        categories = {cat['id']: cat for cat in data.get('categories', [])}
        priorities = {pri['id']: pri for pri in data.get('priorities', [])}
        executors = {ext['id']: ext for ext in data.get('executors', [])}
        tickets = [ticket.copy() for ticket in data.get('tickets', [])]
        
        # Привязка внешних сущностей к полям заявки для удобства доступа
        for ticket in tickets:
            cat_id = ticket.pop('category_id') if 'category_id' in ticket else None
            pri_id = ticket.pop('priority_id') if 'priority_id' in ticket else None
            exec_id = ticket.pop('executor_id') if 'executor_id' in ticket else None
            
            if cat_id and cat_id in categories:
                ticket['category'] = categories[cat_id]
            elif cat_id is not None:
                print(f"Предупреждение: категория {cat_id} не найдена")
            
            if pri_id and pri_id in priorities:
                ticket['priority'] = priorities[pri_id]
            elif pri_id is not None:
                print(f"Предупреждение: приоритет {pri_id} не найден")
                
            if exec_id and exec_id in executors:
                ticket['executor'] = executors[exec_id]
            elif exec_id is not None:
                print(f"Предупреждение: исполнитель {exec_id} не найден")
        
        return {'categories': categories, 'priorities': priorities, 'executors': executors, 'tickets': tickets}
    except json.JSONDecodeError as e:
        sys.stderr.write(f"Ошибка парсинга JSON: {e}\n")
        return None

# Пример использования (раскомментируйте для тестирования):
if __name__ == "__main__":
    sample_json = '''
{
  "categories": [{"id": 1, "name": "IT", "color": "#007bff"}],
  "priorities": [{"id": 1, "level": "high", "label": "Высокий"}],
  "executors": [{"id": 1, "name": "Иванов И.И."}],
  "tickets": [
    {"category_id": 1, "priority_id": 1, "executor_id": 1, 
     "title": "Ошибка входа", "status": "open", "description": "Пользователи не могут войти"}
  ]
}'''

    loaded_data = load_initial_data(sample_json)
    if loaded_data:
        print(f"Загружено {len(loaded_data['tickets'])} заявок.")
