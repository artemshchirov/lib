import sqlite3
conn = sqlite3.connect("students_db.db")  # connect to db or create new

cursor = conn.cursor()

cursor.execute("CREATE TABLE students (first_name TEXT, last_name TEXT, age INTEGER);")
insert_query = "INSERT INTO students VALUES ('James', 'Brown', 21)"

first_name = 'Jarry'
last_name = 'Grey'
age = 36

# Bad approach! SQL injection danger!
# insert_query = f"INSERT INTO students VALUES ('{first_name}', '{last_name}', {age})"

jane = ('Jane', 'Air', 18)
students = [
    ('Bob', 'Marley', 45),
    ('Katty', 'Tomato', 23),
    ('Aleks', 'Ostin', 20)
]

# Good approach!
insert_query = "INSERT INTO students VALUES (?, ?, ?)"

cursor.execute(insert_query, (first_name, last_name, age))
cursor.execute(insert_query, jane)

for student in students:
    cursor.execute(insert_query, student)
# or
cursor.executemany(insert_query, students)

conn.commit()

conn.close()
