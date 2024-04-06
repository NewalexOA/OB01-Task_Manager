class Task:
    def __init__(self):
        self.tasks = []

    def add_task(self, description, due_date, status=False):
        self.tasks.append({"description": description, "due_date": due_date, "status": status})

    def mark_as_done(self, description):
        for task in self.tasks:
            if task["description"] == description:
                task["status"] = True
                break

    def current_tasks(self):
        return [task for task in self.tasks if not task["status"]]


task_manager = Task()
task_manager.add_task("Задача 1", "2024-04-07")
task_manager.add_task("Задача 2", "2024-05-01")
task_manager.mark_as_done("Задача 1")

print("Текущие задачи:")
for task in task_manager.current_tasks():
    print(task["description"], "-", task["due_date"])
