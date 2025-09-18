-- Enable UUID extension
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- Drop the old table
DROP TABLE IF EXISTS tasks CASCADE;

-- Recreate the tasks table
CREATE TABLE tasks (
    task_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    title VARCHAR(255) NOT NULL,
    description TEXT,
    due_date TIMESTAMP NOT NULL,
    priority VARCHAR(10) CHECK (priority IN ('Low', 'Medium', 'High')) DEFAULT 'Medium',
    status VARCHAR(15) CHECK (status IN ('Pending', 'In Progress', 'Completed')) DEFAULT 'Pending',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);