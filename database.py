import sqlite3

# Create Database and Tables
conn = sqlite3.connect("guardian.db")
cursor = conn.cursor()

# Users Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    phone TEXT,
    email TEXT,
    address TEXT,
    guardian_name TEXT,
    guardian_phone TEXT
)
""")

# History Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS history(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT,
    time TEXT,
    status TEXT
)
""")

conn.commit()
conn.close()

print("Database Created Successfully!")


# -------------------------
# Add User Function
# -------------------------
def add_user(name, phone, email, address, guardian_name, guardian_phone):

    conn = sqlite3.connect("guardian.db")
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO users
    (name, phone, email, address, guardian_name, guardian_phone)
    VALUES (?, ?, ?, ?, ?, ?)
    """, (
        name,
        phone,
        email,
        address,
        guardian_name,
        guardian_phone
    ))

    conn.commit()
    conn.close()