def calculate_developer_capacity(
        working_days: int = 10,
        hours_per_day: int = 8,
        buffer_ratio: float = 0.20) -> float:
    """Расчет плановой емкости разработчика (из ПР1)."""
    total_hours = working_days * hours_per_day
    planned_capacity = total_hours * (1.0 - buffer_ratio)
    return planned_capacity


def add_developer(
        developers: list[dict],
        name: str,
        role: str,
        max_capacity: float) -> None:
    """Добавить разработчика в список."""
    new_id = 1 if not developers else max(
        d.get("id", 0) for d in developers) + 1
    developers.append({
        "id": new_id,
        "name": name,
        "role": role,
        "max_capacity": max_capacity
    })


def find_developer(developers: list[dict], query: str) -> list[dict]:
    """Найти разработчиков по подстроке имени."""
    query_lower = query.lower()
    return [d for d in developers if query_lower in d.get("name", "").lower()]


def show_developers(developers: list[dict]) -> None:
    """Вывести список разработчиков."""
    if not developers:
        print("Список разработчиков пуст.")
        return
    print(f"{'ID':<5} | {'Имя':<20} | {'Роль':<25} | {'Емкость (ч)':<10}")
    print("-" * 70)
    for d in developers:
        print(
            f"{
                d['id']:<5} | {
                d['name']:<20} | {
                d['role']:<25} | {
                    d['max_capacity']:<10.1f}")


def sort_developers_by_capacity(developers: list[dict]) -> list[dict]:
    """Отсортировать разработчиков по убыванию емкости."""
    return sorted(
        developers,
        key=lambda d: d.get(
            "max_capacity",
            0),
        reverse=True)
