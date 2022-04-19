import sqlite3
from collections import namedtuple

from database import Database


connection = sqlite3.connect('borrow_book.db')


Entity = namedtuple('Entity', 'name book_title return_at')


def get_borrowers_by_return_date(connection, return_at):
    entities = []
    with Database(connection) as database:
        database.cursor.execute('''
        SELECT
            name
            , book_title
            , return_at
        FROM borrows
        WHERE return_at < ?''', (return_at, ))

        for name, book_title, return_at in database.cursor.fetchall():
            entities.append(Entity(name, book_title, return_at))
    return entities


