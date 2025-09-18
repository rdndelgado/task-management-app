from datetime import datetime
from typing import List, Optional
from schemas.TaskSchema import PriorityLevel, Status
from modules.task import Task
import psycopg2
from config import DB_CONFIG

class TaskManager:
    def __init__(self) -> None:
        self.tasks: List[Task] = []

    @staticmethod
    def add_task(task: Task):
        """Insert a new task into the database using SQL script"""
        conn = psycopg2.connect(**DB_CONFIG)
        cur = conn.cursor()

        # Load insert query from SQL file
        with open("queries/insert_task.sql", "r") as f:
            insert_sql = f.read()

        cur.execute(
            insert_sql,
            (
                task.title,
                task.description,
                task.due_date,
                task.priority.value,
                task.status.value
            ),
        )

        conn.commit()
        cur.close()
        conn.close()
        print(f"Task '{task.title}' added to DB.")

    @staticmethod
    def list_tasks(
        priority: Optional[PriorityLevel] = None,
        status: Optional[Status] = None,
        due_before: Optional[datetime] = None,
    ) -> List[Task]:
        conn = psycopg2.connect(**DB_CONFIG)
        cur = conn.cursor()

        with open("queries/select_tasks.sql", "r") as f:
            base_query = f.read()

        filters = []
        params = []

        if priority:
            filters.append("AND priority = %s")
            params.append(priority.value)
        if status:
            filters.append("AND status = %s")
            params.append(status.value)
        if due_before:
            filters.append("AND due_date <= %s")
            params.append(due_before)

        query = f"{base_query} {' '.join(filters)} ORDER BY due_date ASC"

        cur.execute(query, tuple(params))
        rows = cur.fetchall()

        tasks = [
            Task(
                task_id=row[0],
                title=row[1],
                description=row[2],
                due_date=row[3],
                priority=PriorityLevel(row[4]),
                status=Status(row[5]),
                created_at=row[6],
            )
            for row in rows
        ]

        cur.close()
        conn.close()
        return tasks

    @staticmethod
    def update_task(task: Task) -> None:
        """Update an existing task in the database"""
        if not task.task_id:
            raise ValueError("Task must have a task_id to be updated")

        conn = psycopg2.connect(**DB_CONFIG)
        cur = conn.cursor()

        with open("queries/update_task.sql", "r") as f:
            update_sql = f.read()

        cur.execute(
            update_sql,
            (
                task.title,
                task.description,
                task.due_date,
                task.priority.value,
                task.status.value,
                task.task_id,
            ),
        )

        conn.commit()
        cur.close()
        conn.close()
        print(f"✅ Task {task.task_id} updated successfully")

    @staticmethod
    def complete_task(task_id: str) -> bool:
        """Mark a task as completed in the database"""
        conn = psycopg2.connect(**DB_CONFIG)
        cur = conn.cursor()

        with open("queries/complete_task.sql", "r") as f:
            complete_sql = f.read()

        cur.execute(complete_sql, (task_id,))
        updated_rows = cur.rowcount  # how many rows were affected

        conn.commit()
        cur.close()
        conn.close()

        if updated_rows > 0:
            print(f"✅ Task {task_id} marked as Completed")
            return True
        else:
            print(f"⚠️ Task {task_id} not found")
            return False

    @staticmethod
    def delete_task(task_id: str) -> bool:
        """Delete a task from the database by ID"""
        conn = psycopg2.connect(**DB_CONFIG)
        cur = conn.cursor()

        with open("queries/delete_task.sql", "r") as f:
            delete_sql = f.read()

        cur.execute(delete_sql, (task_id,))
        deleted_rows = cur.rowcount  # number of rows removed

        conn.commit()
        cur.close()
        conn.close()

        if deleted_rows > 0:
            print(f"🗑️ Task {task_id} deleted successfully")
            return True
        else:
            print(f"⚠️ Task {task_id} not found")
            return False