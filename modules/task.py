from datetime import datetime
from typing import Optional
from schemas.TaskSchema import PriorityLevel, Status


class Task:
    def __init__(
        self,
        title: str,
        description: str,
        due_date: datetime,
        priority: PriorityLevel,
        status: Status,
        task_id: Optional[str] = None,
        created_at: Optional[datetime] = None
    ):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.due_date = due_date
        self.priority = priority
        self.status = status
        self.created_at = created_at