import sqlite3
import os

DB_FILE = "goals.db"

def init_db():
    if os.path.exists(DB_FILE):
        os.remove(DB_FILE)
    
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    
    # Projects/Goals Table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS projects (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        category TEXT, -- Business, Health, etc.
        type TEXT, -- Pillar, One-off, Side Quest
        status TEXT DEFAULT 'Active',
        file_path TEXT
    )
    ''')
    
    # Tasks Table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        project_id INTEGER,
        title TEXT NOT NULL,
        status TEXT DEFAULT 'pending', -- pending, done, archived
        deadline DATE,
        created_at DATE DEFAULT CURRENT_DATE,
        FOREIGN KEY(project_id) REFERENCES projects(id)
    )
    ''')
    
    # Seed Data (Generic Template)
    
    # 1. Example Business Project
    cursor.execute("INSERT INTO projects (name, category, type, status, file_path) VALUES (?, ?, ?, ?, ?)",
                   ("Example Business Project", "Business", "Pillar", "Active", "Pillars/pillar-template.md"))
    proj_id = cursor.lastrowid
    
    cursor.execute("INSERT INTO tasks (project_id, title, status, deadline) VALUES (?, ?, ?, ?)",
                   (proj_id, "Define Strategy", "done", "2026-01-01"))
    cursor.execute("INSERT INTO tasks (project_id, title, status, deadline) VALUES (?, ?, ?, ?)",
                   (proj_id, "First Outreach", "pending", "2026-02-01"))

    conn.commit()
    conn.close()
    print("goals.db initialized successfully.")

if __name__ == "__main__":
    init_db()

