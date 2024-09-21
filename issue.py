def create_transactions_table():
    CURSOR.execute("""
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            book_id INTEGER,
            user_id INTEGER,
            borrow_date DATE,
            return_date DATE,
            FOREIGN KEY (book_id) REFERENCES books(id)
        )
    """)
    CONN.commit()
    print('Transactions table was added successfully.')
    CONN.close()
