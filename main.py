from datetime import datetime


class Task:
    def __init__(self, description, due_date):
        self.description = description
        self.due_date = due_date
        self.completed = False

    def mark_completed(self):
        self.completed = True

    def __repr__(self):
        status = "Выполнено" if self.completed else "Не выполнено"
        return f"{self.description} (Срок: {self.due_date}) - {status}"


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self):
        description = input("Введите описание задачи: ")

        current_date = datetime.now().strftime("%d-%m-%Y")
        print(f"Текущая дата: {current_date}")

        due_date = input("Введите срок выполнения задачи (формат ДД-ММ-ГГГГ): ")
        new_task = Task(description, due_date)
        self.tasks.append(new_task)
        print(f"Задача '{description}' добавлена.")

    def show_tasks(self):
        if not self.tasks:
            print("Список задач пуст.")
        else:
            print("Текущие задачи:")
            for i, task in enumerate(self.tasks, 1):
                print(f"{i}. {task}")

    def mark_task_completed(self):
        self.show_tasks()
        task_number = int(input("Введите номер задачи, которую хотите отметить как выполненную: "))
        if 0 < task_number <= len(self.tasks):
            self.tasks[task_number - 1].mark_completed()
            print(f"Задача '{self.tasks[task_number - 1].description}' отмечена как выполненная.")
        else:
            print("Неправильный номер задачи.")

    def delete_task(self):
        self.show_tasks()
        task_number = int(input("Введите номер задачи, которую хотите удалить: "))
        if 0 < task_number <= len(self.tasks):
            task = self.tasks.pop(task_number - 1)
            print(f"Задача '{task.description}' удалена.")
        else:
            print("Неправильный номер задачи.")


def main():
    manager = TaskManager()
    while True:
        print("\nМеню:")
        print("1. Добавить задачу")
        print("2. Показать задачи")
        print("3. Отметить задачу как выполненную")
        print("4. Удалить задачу")
        print("5. Выйти")
        choice = input("Выберите действие: ")

        if choice == '1':
            manager.add_task()
        elif choice == '2':
            manager.show_tasks()
        elif choice == '3':
            manager.mark_task_completed()
        elif choice == '4':
            manager.delete_task()
        elif choice == '5':
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")


if __name__ == "__main__":
    main()
