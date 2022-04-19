import sqlite3
import pytest

from borrowers import get_borrowers_by_return_date


@pytest.fixture
def create_connection():
    connection = sqlite3.connect(":memory:")
    cursor = connection.cursor()
    cursor.execute("""
    CREATE TABLE 'borrows'(
        id integer primary key autoincrement,
        name TEXT,
        book_title TEXT,
        return_at DATE)"""
    )
    sample_data = [
        (1, "Adam", "Mały Książę", "2021-05-12"),
        (2, "Robert", "Robinson Cruzoe", "2022-10-01"),
        (3, "Marian", "Stary człowiek i morze", "2023-01-02"),
    ]
    cursor.executemany("INSERT INTO borrows VALUES (?, ?, ?, ?)", sample_data)
    return connection


def test_borrows(create_connection):
    borrowers = get_borrowers_by_return_date(connection=create_connection, return_at="2022-10-02")
    assert len(borrowers) == 2
    assert type(borrowers) is list
    assert borrowers[0].name == 'Adam'
    assert borrowers[1].name == 'Robert'
