from modules import task, manager
from schemas.TaskSchema import PriorityLevel, Status
from datetime import datetime

TaskManager = manager.TaskManager()

tasks = TaskManager.list_tasks()
for t in tasks:
    print(f"Task: {t.task_id}")
