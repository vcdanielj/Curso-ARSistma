import sqlite3

bd = sqlite3.connect("bd_productos.sqlite3")

cursor = bd.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS productos (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               nombre TEXT NOT NULL,
               precio REAL NOT NULL,
               cantidad INTEGER NOT NULL
               )''')

bd.commit()