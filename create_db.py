import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

cursor.executescript("""
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    password TEXT
);
INSERT INTO users(username,password) VALUES("admin","admin123");

CREATE TABLE vehicles (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    vehicle_no TEXT,
    driver TEXT
);

CREATE TABLE fuel_transactions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT,
    vehicle_id INTEGER,
    fuel TEXT,
    litres REAL,
    type TEXT,
    remarks TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(vehicle_id) REFERENCES vehicles(id)
);
""")

conn.commit()
conn.close()

print("🚀 Database created successfully! ✔ database.db is ready.")
