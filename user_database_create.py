import sqlite3
connection = sqlite3.connect("user.db")
cursor = connection.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS users (username TEXT, password TEXT)")
connection.commit()