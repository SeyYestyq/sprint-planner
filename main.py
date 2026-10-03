import os
from datetime import date, timedelta
from storage import load_developers, save_developers, load_tasks, save_tasks
from utils import input_int, input_float, generate_release_name
from developers import (
    add_developer, find_developer, show_developers,
    calculate_developer_capacity, sort_developers_by_capacity
)
from tasks import (
    add_task, cancel_task, show_tasks,
    get_developer_workload, is_developer_available, validate_sprint_workload
)

DEV_FILE = "data/developers.json"
TASKS_FILE = "data/tasks.json"


def main():
    # Создаем папку data, если ее нет
    if not os.path.exists("data"):
        os.makedirs("data")

    developers = load_developers(DEV_FILE)
    tasks = load_tasks(TASKS_FILE)

    while True:
        print("\n=== Сервис планирования спринтов ===")
        print("1. Показать разработчиков")
        print("2. Найти разработчика по имени")
        print("3. Добавить разработчика")
        print("4. Проверить загрузку разработчика")
        print("5. Назначить задачу")
        print("6. Отменить задачу")
        print("7. Показать все задачи спринта")
        print("8. Сгенерировать имя релиза")
        print("0. Выход")

        choice = input("Выберите действие: ").strip()

        if choice == "1":
            sorted_devs = sort_developers_by_capacity(developers)
            show_developers(sorted_devs)

        elif choice == "2":
            query = input("Введите имя для поиска: ").strip()
            found = find_developer(developers, query)
            show_developers(found)

        elif choice == "3":
            name = input("Имя разработчика: ").strip()
            role = input("Роль: ").strip()
            print("Рассчитать емкость автоматически? (д/н)")
            if input().strip().lower() in ['д', 'y']:
                days = input_int("Количество рабочих дней [10]: ")
                hours = input_int("Часов в день [8]: ")
                cap = calculate_developer_capacity(days, hours)
                print(f"Расчетная емкость: {cap} ч.")
            else:
                cap = input_float("Плановая емкость (ч): ")
            add_developer(developers, name, role, cap)
            save_developers(DEV_FILE, developers)
            print("Разработчик добавлен.")

        elif choice == "4":
            dev_id = input_int("Введите ID разработчика: ")
            dev = next((d for d in developers if d["id"] == dev_id), None)
            if not dev:
                print("Разработчик не найден.")
                continue
            workload = get_developer_workload(tasks, dev_id)
            status = validate_sprint_workload(workload, dev["max_capacity"])
            print(f"Разработчик: {dev['name']}")
            print(f"Текущая загрузка: {workload} / {dev['max_capacity']} ч.")
            print(status)

        elif choice == "5":
            dev_id = input_int("Введите ID разработчика: ")
            dev = next((d for d in developers if d["id"] == dev_id), None)
            if not dev:
                print("Разработчик не найден.")
                continue
            title = input("Название задачи: ").strip()
            hours = input_float("Оценка времени (ч): ")

            if is_developer_available(
                    tasks, dev_id, hours, dev["max_capacity"]):
                add_task(tasks, dev_id, title, hours)
                save_tasks(TASKS_FILE, tasks)
                print("Задача успешно добавлена.")
            else:
                print(
                    "Ошибка: Добавление задачи приведет "
                    "к превышению емкости разработчика!"
                )

        elif choice == "6":
            task_id = input_int("Введите ID задачи для отмены: ")
            if cancel_task(tasks, task_id):
                save_tasks(TASKS_FILE, tasks)
                print("Задача отменена.")
            else:
                print("Задача не найдена.")

        elif choice == "7":
            show_tasks(tasks)

        elif choice == "8":
            sprint_end = date.today() + timedelta(days=14)
            name = generate_release_name(sprint_end)
            print(f"Имя релиза по умолчанию (через 14 дней): {name}")

        elif choice == "0":
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор.")


if __name__ == "__main__":
    main()
