import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

DB_CONFIG = {
    "dbname": os.getenv("POSTGRES_DB"),
    "user": os.getenv("POSTGRES_USER"),
    "password": os.getenv("POSTGRES_PASSWORD"),
    "host": os.getenv("POSTGRES_HOST", "localhost"),  # default to localhost
    "port": os.getenv("POSTGRES_PORT", "5432"),
}

CONTAINER_NAME = os.getenv("CONTAINER_NAME", "taskdb")
POSTGRES_IMAGE = os.getenv("POSTGRES_IMAGE", "postgres:15")