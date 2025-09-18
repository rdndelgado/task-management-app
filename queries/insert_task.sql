INSERT INTO tasks (
    title,
    description,
    due_date,
    priority,
    status
) VALUES (
    %s, %s, %s, %s, %s
);