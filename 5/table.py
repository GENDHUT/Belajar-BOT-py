import sqlite3

connection =sqlite3.connect('user.db')
cursor = connection.cursor()

create_table_query = """
    CREATE TABLE IF NOT EXISTS users(
        id intiger primary key,
        first_name text,
        last_name text,
        phone_number text
    );
"""

cursor.execute(create_table_query)
connection.commit()
connection.close()

sample_data_query = """
    INSERT INTO users (id ,first_name ,last_name ,phone_number )
    VALUES ( ?, ?, ?, ?)
"""

sample_data = [
                (1, 'test', '1', '08121239457568'),
                (2, 'test', '2', '08121239457568'),
                (3, 'test', '3', '08121239457568'),
                (4, 'test', '4', '08121239457568'),
               ]

# with sqlite3.connect('user.db') as connection:
#     cursor = connection.cursor()
#     cursor.executemany(sample_data_query,sample_data)

fetch_Data_query = """
    SELECT id, first_name, last_name, phone_number FROM users
"""

rows = []

with sqlite3.connect('user.db') as connection:
    cursor = connection.cursor()
    cursor.execute(fetch_Data_query)
    rows = cursor.fetchall()
    
for row in rows:
    print(f'ID:{row[0]},FN:{row[1]},LN:{row[2]},PN:{row[3]}', end='\n')