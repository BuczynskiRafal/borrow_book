import email
import smtplib
import ssl
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
# print(borrowers)


ssl_enable = False
port = 2525
smtp_server = 'smtp.mailtrap.io'
username = '96739960872c76'
password = '155d56a76d963e'

sender = 'Kacper Sieradziński <kacper@dokodu.it>'
receiver = 'Rafał B <buczynski.rafal2@gmail.com>'

subject = 'test message'
message = email.message_from_string(f"""Subject: {subject}
To: {receiver}
From: {sender}

To jest wiadomość testowa.
""")
message.set_charset('utf-8')

if not ssl_enable:
    connection = smtplib.SMTP(smtp_server, port)
else:
    context = ssl.create_default_context()
    connection = smtplib.SMTP_SSL(smtp_server, port, context)

connection.login(username, password)
connection.sendmail(sender, receiver, message.as_string())
connection.close()


class EmailSender:
    def __init__(self, port, smtp_server, credentials, ssl_enable = False):
        self.port = port
        self.smtp_server = smtp_server
        self.ssl_enable = ssl_enable
        self.credentials = credentials
        self.connection = None

    def __enter__(self):
        if not self.ssl_enable:
            self.connection = smtplib.SMTP(self.smtp_server, self.port)
        else:
            context = ssl.create_default_context()
            self.connection = smtplib.SMTP_SSL(self.smtp_server, self.port, context)

        self.connection.login(self.credentials.username, self.credentials.password)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.close()