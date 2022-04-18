import sqlite3


class Database:
    def __init__(self, connection):
        self.connection = connection
        self.cursor = None

    def __enter__(self):
        self.cursor = self.connection.cursor()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if isinstance(exc_val, Exception):
            self.connection.rollback()
        else:
            connection.commit()

        connection.close()


connection = sqlite3.connect('borrow_book.db')

with Database(connection=connection) as db:
    db.cursor.execute('''
CREATE TABLE 'borrows'(
id integer primary key autoincrement,
name TEXT,
book_title TEXT
book_return_date
)
''')
