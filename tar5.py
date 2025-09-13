def task_manager():
    tasks = {}  # מצב פנימי של המנהל

    def add_task(name, status="incomplete"):
        nonlocal tasks
        # בלי שינוי במקום: יוצרים מילון חדש עם הערך/עדכון
        tasks = {**tasks, name: status}
        return dict(tasks)

    def get_tasks():
        # מחזיר עותק (שלא יוכלו לשנות מבחוץ)
        return dict(tasks)

    def complete_task(name):
        nonlocal tasks
        if name in tasks:
            tasks = {**tasks, name: "complete"}
        return dict(tasks)

    return {
        "add_task": add_task,
        "get_tasks": get_tasks,
        "complete_task": complete_task,
    }
tasks_manager = task_manager()

tasks_manager["add_task"]("Write email")
tasks_manager["add_task"]("Shopping", "in progress")
tasks_manager["add_task"]("Homework")

print(tasks_manager["get_tasks"]())
# {'Write email': 'incomplete', 'Shopping': 'in progress', 'Homework': 'incomplete'}

tasks_manager["complete_task"]("Write email")
print(tasks_manager["get_tasks"]())
# {'Write email': 'complete', 'Shopping': 'in progress', 'Homework': 'incomplete'}
