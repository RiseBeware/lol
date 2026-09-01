# === Stage 33: Добавь откат последнего действия там, где это разумно ===
# Project: TicketLedger
import re

def add_rollback_support():
    """Добавить возможность отката последнего действия."""
    # Пример отката: удаление последнего элемента из списка
    def undo_last(lst):
        if lst:
            lst.pop()
        return lst
    # Пример отката: восстановление предыдущего значения
    def undo_last_value(current, previous):
        if previous is not None:
            return previous
        return current
    # Пример отката: отмена последнего изменения в словаре
    def undo_last_change(data, key):
        if key in data:
            del data[key]
        return data
    # Пример отката: отмена последнего изменения в строке
    def undo_last_change_str(current, previous):
        if previous is not None:
            return previous
        return current
    return undo_last, undo_last_value, undo_last_change, undo_last_change_str
