import sqlite3
import os
DB_PATH = os.getenv("DB_PATH","/mnt/data/smart_ci_monitor.db")

def get_conn():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS builds (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        job_name TEXT,
        build_number INTEGER,
        result TEXT,
        timestamp INTEGER
    )''')
    conn.commit()
    conn.close()

if __name__ == '__main__':
    init_db()
