import sqlite3

'''Для решения этой задачи вам понадобится решение предыдущей'''

from moduleSql import *

'''Для решения необходимо дополнить существующий код:
Удалите из базы данных not_telegram.db запись с id = 6.'''

#cursor.execute("DELETE FROM Users WHERE id = 6")

'''Подсчитать общее количество записей'''

cursor.execute("SELECT COUNT(*) FROM Users")
total_users = cursor.fetchone()[0]

'''Посчитать сумму всех балансов.'''

cursor.execute("SELECT SUM(balance) FROM Users")
all_balance = cursor.fetchone()[0]

'''Вывести в консоль средний баланс всех пользователей.'''

print(f'COUNT(*) = {total_users}')
print(f'SUM(balance) = {all_balance}')
print(f'Средний баланс: {all_balance/total_users}')

#Или вот так
cursor.execute("SELECT AVG(balance) FROM Users")
avg_balance = cursor.fetchone()[0]
print(f"Функция 'AVERAGE' тоже успешно справилась {avg_balance}")

'''Пример результата выполнения программы:
Выполняемый код:
# Код из предыдущего задания
# Удаление пользователя с id=6
# Подсчёт кол-ва всех пользователей
# Подсчёт суммы всех балансов
Вывод на консоль:
700.0'''
connection.commit()
connection.close()