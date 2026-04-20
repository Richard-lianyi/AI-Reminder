from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
import sqlite3
from datetime import datetime
from database import init_db

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

init_db()


def row_to_dict(row):
    return {
        "id": row[0],
        "task": row[1],
        "time": row[2],
        "done": row[3],
        "notified": row[4]
    }


@app.post("/add")
def add_reminder(task: str, time: str):
    task = task.strip()

    if not task:
        return {"status": "error", "message": "Task cannot be empty"}

    try:
        datetime.strptime(time, "%Y-%m-%d %H:%M")
    except ValueError:
        return {"status": "error", "message": "Invalid time format. Use YYYY-MM-DD HH:MM"}

    conn = sqlite3.connect("reminders.db")
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO reminders (task, time, done, notified) VALUES (?, ?, 0, 0)",
        (task, time)
    )

    conn.commit()
    conn.close()

    return {"status": "added"}


@app.get("/list")
def list_reminders():
    conn = sqlite3.connect("reminders.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM reminders WHERE done = 0 AND notified = 0 ORDER BY time")
    rows = cursor.fetchall()

    conn.close()

    return [row_to_dict(row) for row in rows]

@app.get("/notified")
def notified_reminders():
    conn = sqlite3.connect("reminders.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM reminders WHERE done = 0 AND notified = 1 ORDER BY time")
    rows = cursor.fetchall()

    conn.close()

    return [row_to_dict(row) for row in rows]

@app.get("/completed")
def completed_reminders():
    conn = sqlite3.connect("reminders.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM reminders WHERE done = 1 ORDER BY time")
    rows = cursor.fetchall()

    conn.close()

    return [row_to_dict(row) for row in rows]


@app.put("/complete/{reminder_id}")
def complete_reminder(reminder_id: int):
    conn = sqlite3.connect("reminders.db")
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE reminders SET done = 1 WHERE id = ?",
        (reminder_id,)
    )

    conn.commit()
    conn.close()

    return {"status": "completed"}


@app.delete("/delete/{reminder_id}")
def delete_reminder(reminder_id: int):
    conn = sqlite3.connect("reminders.db")
    cursor = conn.cursor()

    cursor.execute("DELETE FROM reminders WHERE id = ?", (reminder_id,))

    conn.commit()
    conn.close()

    return {"status": "deleted"}


@app.get("/")
def read_index():
    return FileResponse("index.html")
