import sqlite3


connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
''')

'''Заполните таблицу 10 записями:'''
# for i in range(1, 11):
#     cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)", (f"newuser{i}", f"example{i}@gmail.com", 10*i, 1000))

'''Обновите balance у каждой 2ой записи начиная с 1ой на 500:'''
cursor.execute("UPDATE Users SET balance = ? WHERE id % 2 = 1", (500,))

'''Удалите каждую 3ую запись в таблице начиная с 1ой:'''
for j in range(1, 11, 3):
    cursor.execute("DELETE FROM Users WHERE id = ?", (j,))

'''Сделайте выборку всех записей при помощи fetchall(), где возраст не равен 60 и выведите их в консоль в следующем формате (без id):
Имя: <username> | Почта: <email> | Возраст: <age> | Баланс: <balance>'''
cursor.execute('SELECT * FROM Users WHERE age != 60')
users = cursor.fetchall()
for u in users:
    print(f'Имя: {u[1]} | Почта: {u[2]} | Возраст: {u[3]} | Баланс: {u[4]}')

connection.commit()
connection.close()