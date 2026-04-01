from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
import sqlite3
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

@app.post("/add")
def add_reminder(task: str, time: str):
    conn = sqlite3.connect("reminders.db")
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO reminders (task, time, done) VALUES (?, ?, 0)",
        (task, time)
    )

    conn.commit()
    conn.close()

    return {"status": "added"}

@app.get("/list")
def list_reminders():
    conn = sqlite3.connect("reminders.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM reminders WHERE done = 0")
    rows = cursor.fetchall()

    conn.close()

    return rows

@app.get("/completed")
def completed_reminders():
    conn = sqlite3.connect("reminders.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM reminders WHERE done = 1")
    rows = cursor.fetchall()

    conn.close()

    return rows

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