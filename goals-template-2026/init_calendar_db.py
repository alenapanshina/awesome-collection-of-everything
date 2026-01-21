import sqlite3
import os

DB_FILE = "calendar.db"

def init_db():
    if os.path.exists(DB_FILE):
        os.remove(DB_FILE)
    
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    
    # Events Table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS events (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        date DATE NOT NULL,
        start_time TEXT, -- HH:MM
        end_time TEXT, -- HH:MM
        location TEXT,
        notes TEXT,
        recurring TEXT -- daily, weekly, monthly, null
    )
    ''')
    
    # Seed Data (Generic Template)
    cursor.execute("INSERT INTO events (title, date, start_time, end_time, recurring) VALUES (?, ?, ?, ?, ?)",
                   ("Weekly Review", "2026-01-01", "09:00", "10:00", "weekly"))
    
    conn.commit()
    conn.close()
    print("calendar.db initialized successfully.")

if __name__ == "__main__":
    init_db()

