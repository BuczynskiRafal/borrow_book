import sqlite3
from database import Database
from borrowers import get_borrowers_by_return_date
connection = sqlite3.connect('borrow_book.db')


def setup(connection):
    with Database(connection) as database:
        database.cursor.execute('''
    CREATE TABLE 'borrows'(
    id integer primary key autoincrement,
    name TEXT,
    book_title TEXT,
    return_at DATE)''')


borrowers = get_borrowers_by_return_date(connection=connection, return_at='2022-12-11')
print(borrowers)
