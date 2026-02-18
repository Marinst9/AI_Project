import sqlite3

conn = sqlite3.connect('emocii.db')
cursor = conn.cursor()

cursor.execute("SELECT * FROM analizi")
rows = cursor.fetchall()

print("--- ПОДАТОЦИ ОД SQL БАЗАТА ---")
for row in rows:
    print(f"ID: {row[0]} | Емоција: {row[2]} | Текст: {row[1]}")

conn.close()