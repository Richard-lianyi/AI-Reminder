import sqlite3


def init_db():
    conn = sqlite3.connect("reminders.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS reminders (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        task TEXT,
        time TEXT,
        done INTEGER DEFAULT 0,
        notified INTEGER DEFAULT 0 
    )
    """)

    cursor.execute("PRAGMA table_info(reminders)")
    columns = [column[1] for column in cursor.fetchall()]

    if "notified" not in columns:
        cursor.execute("ALTER TABLE reminders ADD COLUMN notified INTEGER DEFAULT 0")

    conn.commit()
    conn.close()
