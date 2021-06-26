import sqlite3
conn = sqlite3.connect("users_db.db")
cursor = conn.cursor()

# create_query = "CREATE TABLE users (user_name TEXT, user_password TEXT)"

users = [

    ('jack123', 'qwerty'),
    ('jane', 'rewq'),
    ('bob421', 'asdf')

]
insert_query = "INSERT INTO users VALUES (?, ?)"

user_name = input("Input your name: ")
user_password = input("Input your password: ")

# Danger SQL injection!
# select_query = f"SELECT * FROM users WHERE user_name='{user_name}' AND user_password='{user_password}'"

# Good approach
select_query = f"SELECT * FROM users WHERE user_name= ? AND user_password= ?"

cursor.execute(select_query, (user_name, user_password))

data = cursor.fetchone()
if data:
    print('You are logged in')
else:
    print('Please try again')

conn.commit()
conn.close()
