import sqlite3

def init_db():
    conn = sqlite3.connect("reminders.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS reminders (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        task TEXT,
        time TEXT,
        done INTEGER
    )
    """)

    conn.commit()
    conn.close()