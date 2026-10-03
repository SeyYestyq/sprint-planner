from datetime import date


def input_int(prompt: str) -> int:
    """Запросить у пользователя целое число с обработкой ошибок."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Ошибка: введите целое число.")


def input_float(prompt: str) -> float:
    """Запросить у пользователя вещественное число с обработкой ошибок."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Ошибка: введите число.")


def generate_release_name(
        sprint_end: date,
        is_prerelease: bool = False) -> str:
    """Генерация регламентного имени релиза (из ПР1)."""
    date_str = sprint_end.strftime("%Y-%m-%d")
    if is_prerelease:
        return f"crafttalk-{date_str}-prerelease"
    return f"crafttalk-{date_str}"
