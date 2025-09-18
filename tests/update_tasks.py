from datetime import datetime
from schemas.TaskSchema import PriorityLevel, Status
from modules.task import Task
from modules.manager import TaskManager

# Imagine this task was already added and has a task_id
new_task = Task(
    title="Write blog post",
    description="Draft a blog post about AI",
    due_date=datetime(2025, 9, 20),
    priority=PriorityLevel.HIGH,
    status=Status.PENDING,
    task_id="c9f5b1d6-5c1f-4d1a-a2f1-65a59d1f1234"  # fetched from DB
)

# Update some fields
new_task.title = "Write AI blog post"
new_task.status = Status.IN_PROGRESS

# Save changes to DB
TaskManager.update_task(new_task)