import sqlite3

CONN = sqlite3.connect('bookstore.db')
CURSOR = CONN.cursor()