import json
import os


def load_operation_json(data_file):
    """
    Загружает данные из JSON-файла.
    """
    file_path = os.path.join(data_file)

    # Проверяем, существует ли файл
    if not os.path.exists(file_path):
        return []

    # Открываем и читаем файл
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
            # Проверяем, что данные являются списком
            if isinstance(data, list):
                return data
            else:
                return []
    except (json.JSONDecodeError, OSError):
        # Обрабатываем ошибки декодирования JSON и ошибки файловой системы
        return []
