UPDATE tasks
SET
    title = %s,
    description = %s,
    due_date = %s,
    priority = %s,
    status = %s
WHERE task_id = %s;