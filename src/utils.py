import json
import logging
import os

utils_logger = logging.getLogger(__name__)


def load_operation_json(data_file):
    """
    Загружает данные из JSON-файла.
    """
    file_path = os.path.join(data_file)

    # Логируем начало
    utils_logger.debug(f"Начало загрузки данных из файла: {file_path}")

    # Проверяем, существует ли файл
    if not os.path.exists(file_path):
        utils_logger.error(f"Файл не найден: {file_path}")
        return []

    # Открываем и читаем файл
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
            # Проверяем, что данные являются списком
            if isinstance(data, list):
                utils_logger.debug(f"Данные успешно загружены из файла: {file_path}")
                return data
            else:
                utils_logger.error(f"Данные в файле {file_path} не являются списком")
                return []
    except json.JSONDecodeError as e:
        # Логируем ошибку
        utils_logger.error(f"Ошибка декодирования JSON в файле {file_path}: {e}")
        # Обрабатываем ошибки декодирования JSON и ошибки файловой системы
        return []
