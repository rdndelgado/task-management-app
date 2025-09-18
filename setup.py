import subprocess
import time
import psycopg2
from config import DB_CONFIG, CONTAINER_NAME, POSTGRES_IMAGE

"""This file will setup the configuration for the Postgres database using Docker."""

print("Starting PostgreSQL container...")
subprocess.run([
    "docker", "run", "-d",
    "--name", CONTAINER_NAME,
    "-e", f"POSTGRES_USER={DB_CONFIG['user']}",
    "-e", f"POSTGRES_PASSWORD={DB_CONFIG['password']}",
    "-e", f"POSTGRES_DB={DB_CONFIG['dbname']}",
    "-p", f"{DB_CONFIG['port']}:5432",
    POSTGRES_IMAGE
])

print("Initializing Postgres...")
time.sleep(5)

print("Connecting to Postgres...")
conn = psycopg2.connect(**DB_CONFIG)
cur = conn.cursor()

print("Executing SQL script...")
with open("queries/create_table.sql", "r") as f:
    create_table_sql = f.read()
cur.execute(create_table_sql)
print('Table created.')

conn.commit()
cur.close()
conn.close()
print("Setup completed.")