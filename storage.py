import json
import os


def load_data(filename: str, default_data: list) -> list:
    """Универсальная функция загрузки данных из JSON-файла."""
    if not os.path.exists(filename):
        return default_data
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        return default_data


def save_data(filename: str, data: list) -> None:
    """Универсальная функция сохранения данных в JSON-файл."""
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
    except IOError as e:
        print(f"Ошибка при сохранении данных в {filename}: {e}")


def load_developers(filename: str) -> list:
    return load_data(filename, [])


def save_developers(filename: str, developers: list) -> None:
    save_data(filename, developers)


def load_tasks(filename: str) -> list:
    return load_data(filename, [])


def save_tasks(filename: str, tasks: list) -> None:
    save_data(filename, tasks)
