class Task:
    def __init__(self, description, completed=False):
        self.description = description
        self.completed = completed

class DailyTaskList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def update_task(self, task_description, completed=True):
        for task in self.tasks:
            if task.description == task_description:
                task.completed = completed

    def delete_task(self, task_description):
        self.tasks = [task for task in self.tasks if task.description != task_description]

    def get_completion_percentage(self):
        if not self.tasks:
            return 0

        completed_tasks = sum(1 for task in self.tasks if task.completed)
        return (completed_tasks / len(self.tasks)) * 100

daily_tasks = DailyTaskList()

daily_tasks.add_task(Task("study for 1 hour"))
daily_tasks.add_task(Task("Read book for 1 hour"))

daily_tasks.update_task("study for 1 hour")
daily_tasks.update_task("Read book for 1 hour")

daily_tasks.delete_task("Read book for 1 hour")

print("Tasks:")
for task in daily_tasks.tasks:
    status = "Completed" if task.completed else "Not Completed"
    print(f"{task.description}: {status}")

print(f"Completion Percentage: {daily_tasks.get_completion_percentage()}%")
