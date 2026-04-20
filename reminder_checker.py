import sqlite3
import time
from datetime import datetime

while True:
    conn = sqlite3.connect("reminders.db")
    cursor = conn.cursor()

    now = datetime.now().strftime("%Y-%m-%d %H:%M")

    cursor.execute(
        "SELECT id, task FROM reminders WHERE time <= ? AND done = 0 AND notified = 0",
        (now,)
    )

    reminders = cursor.fetchall()

    for r in reminders:
        print("🔔 REMINDER:", r[1])

        cursor.execute(
            "UPDATE reminders SET notified = 1 WHERE id = ?",
            (r[0],)
        )

    conn.commit()
    conn.close()

    time.sleep(60)