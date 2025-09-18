### 🚀 Task Management App – Setup Instructions

#### 1️⃣ Clone the Repository
- `git clone https://github.com/rdndelgado/task-management-app.git`
- `cd task-management-app`

#### 2️ Create and Activate Virtual Environment
Linux / macOS:
- `python3 -m venv venv`
- `source venv/bin/activate`

Windows (PowerShell):
`python -m venv venv`
`venv\Scripts\activate`

#### 3️⃣ Install Requirements

Make sure pip is up to date:

`pip install --upgrade pip`


Install dependencies:

`pip install -r requirements.txt`

#### 4️⃣ Create .env File

In the project root, create .env with the following variables:

POSTGRES_USER=postgres
POSTGRES_PASSWORD=taskdb-mm
POSTGRES_DB=taskmanagerdb
POSTGRES_PORT=5432
CONTAINER_NAME=taskmanager_postgres

#### 5️⃣ Install Docker

If you don’t have Docker installed, download it here:
👉 [Get Docker](https://docs.docker.com/get-docker/)

Make sure it works:

`docker --version`
`docker compose version`

#### 6️⃣ Run Database Setup

This will spin up a Postgres container and create the tasks table using queries/create_table.sql.

`python setup.py`

You should see:

Starting PostgreSQL container...
Initializing Postgres...
Connecting to Postgres...
📄 Executing SQL script...
Setup completed.

#### 7️⃣ Run the App

Finally, start the Task Manager CLI:

`python app.py`

You'll see:

Task Manager
1. Add task
2. List tasks
3. Update task
4. Complete task
5. Delete task
6. Exit

#### 8️⃣ Stop the Database (when finished)
`docker stop taskmanager_postgres`
`docker rm taskmanager_postgres`