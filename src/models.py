# src/models.py
import sqlite3

def connect_db():
    conn = sqlite3.connect('database.db')
    return conn

def create_tables():
    conn = connect_db()
    cursor = conn.cursor()
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS employees (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        position TEXT NOT NULL,
        hourly_rate REAL NOT NULL
    )
    ''')
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS payroll (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        employee_id INTEGER,
        hours_worked REAL NOT NULL,
        month TEXT NOT NULL,
        year INTEGER NOT NULL,
        FOREIGN KEY (employee_id) REFERENCES employees (id)
    )
    ''')
    
    conn.commit()
    conn.close()

if __name__ == '__main__':
    create_tables()
