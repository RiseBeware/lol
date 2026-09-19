# === Stage 44: Добавь функцию резервного копирования файла данных ===
# Project: TicketLedger
import shutil, os

def backup_data_file(path: str, backup_dir: str = "backups") -> str:
    """Создать резервную копию файла данных.
    
    Args:
        path: путь к текущему файлу данных.
        backup_dir: директория для хранения бэкапов.
    
    Returns:
        путь к созданному файлу бэкапа.
    
    Raises:
        FileNotFoundError: если файл данных не существует.
    """
    if not os.path.exists(path):
        raise FileNotFoundError(f"Файл данных не найден: {path}")
    
    os.makedirs(backup_dir, exist_ok=True)
    
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_path = os.path.join(backup_dir, f"{os.path.basename(path)}.{timestamp}.bak")
    
    shutil.copy2(path, backup_path)
    
    return backup_path
