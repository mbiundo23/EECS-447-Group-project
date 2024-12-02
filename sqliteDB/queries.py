import sqlite3
connection = sqlite3.connect('library_database.db')
cursor = connection.cursor()

cursor.execute("SELECT * From PhysicalBook")
results = cursor.fetchall()
print(results)