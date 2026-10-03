def get_developer_workload(tasks: list[dict], developer_id: int) -> float:
    """Получить суммарную загрузку разработчика в часах."""
    return sum(t.get("estimated_hours", 0)
               for t in tasks if t.get("developer_id") == developer_id)


def is_developer_available(
        tasks: list[dict],
        developer_id: int,
        new_task_hours: float,
        max_capacity: float) -> bool:
    """Проверить, не превысит ли новая задача лимит разработчика."""
    current_workload = get_developer_workload(tasks, developer_id)
    return (current_workload + new_task_hours) <= max_capacity


def validate_sprint_workload(
        assigned_hours: float,
        max_capacity: float) -> str:
    """Проверка загрузки разработчика в спринте (из ПР1)."""
    if assigned_hours > max_capacity:
        overload = assigned_hours - max_capacity
        return f"ВНИМАНИЕ: Перегрузка на {overload:.1f} ч! Превышен лимит 80%."
    elif assigned_hours == max_capacity:
        return "Оптимальная загрузка: распределены ровно 80% времени."
    else:
        remaining = max_capacity - assigned_hours
        return f"Загрузка в норме. Можно добавить еще {remaining:.1f} ч задач."


def add_task(
        tasks: list[dict],
        developer_id: int,
        title: str,
        estimated_hours: float) -> None:
    """Добавить задачу в спринт."""
    new_id = 1 if not tasks else max(t.get("id", 0) for t in tasks) + 1
    tasks.append({
        "id": new_id,
        "developer_id": developer_id,
        "title": title,
        "estimated_hours": estimated_hours
    })


def cancel_task(tasks: list[dict], task_id: int) -> bool:
    """Отменить (удалить) задачу."""
    for i, t in enumerate(tasks):
        if t.get("id") == task_id:
            del tasks[i]
            return True
    return False


def show_tasks(tasks: list[dict]) -> None:
    """Вывести список задач."""
    if not tasks:
        print("Список задач пуст.")
        return
    print(f"{'ID':<5} | {'Dev ID':<8} | {'Оценка (ч)':<12} | {'Название'}")
    print("-" * 60)
    for t in tasks:
        print(
            f"{
                t['id']:<5} | {
                t['developer_id']:<8} | {
                t['estimated_hours']:<12.1f} | {
                    t['title']}")
