from __init__ import CURSOR,CONN
from datetime import datetime,date


def create_borrowed_books_table():
    CURSOR.execute("""
        CREATE TABLE IF NOT EXISTS BorrowedBooks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            employee_id INTEGER NOT NULL,
            book_id INTEGER NOT NULL,
            borrow_date DATE NOT NULL,
            return_date DATE,
            returned BOOLEAN DEFAULT FALSE,
            FOREIGN KEY (employee_id) REFERENCES employees(id),
            FOREIGN KEY (book_id) REFERENCES books(id)
        )
    """)
    CONN.commit()
    print("BorrowedBooks table created successfully.")
    CONN.close()

   # create_borrowed_books_table()

   ##############################################################
def borrow_book(employee_id, book_id):
    # Insert a new borrowed book record
    CURSOR.execute("""
        INSERT INTO BorrowedBooks (employee_id, book_id, borrow_date, returned)
        VALUES (?, ?, ?, ?)
    """, (employee_id, book_id, date.today(), False))
    
    # Mark the book as unavailable in the Books table
    CURSOR.execute("""
        UPDATE books SET available = ? WHERE id = ?
    """, (False, book_id))
    
    CONN.commit()
    print(f"Book with ID {book_id} borrowed by Employee {employee_id}.")

###########################################################################

def return_book():
    try:
        # Get inputs from the user
        book_id = int(input("Enter the ID of the book to return: "))
        user_id = int(input("Enter your user ID: "))

        # Check if the book was borrowed by the user and not yet returned
        CURSOR.execute("""
            SELECT * FROM BorrowedBooks 
            WHERE book_id = ? AND user_id = ? AND returned = FALSE
        """, (book_id, user_id))
        
        borrowed_book = CURSOR.fetchone()

        # If no matching record is found
        if borrowed_book is None:
            print("This book was not borrowed by you or has already been returned.")
            return

        # Update the returned status and return date in the BorrowedBooks table
        CURSOR.execute("""
            UPDATE BorrowedBooks
            SET returned = TRUE, return_date = date('now')
            WHERE id = ?
        """, (borrowed_book[0],))  # borrowed_book[0] is the transaction ID in BorrowedBooks

        # Mark the book as available in the books table
        CURSOR.execute("""
            UPDATE books
            SET available = TRUE
            WHERE id = ?
        """, (book_id,))

        # Commit the transaction
        CONN.commit()

        # Notify the user of success
        print(f'Book with ID {book_id} has been returned successfully.')

    except ValueError:
        print("Invalid input. Please enter valid IDs.")
    except Exception as e:
        print(f"An error occurred while returning the book: {e}")
        CONN.rollback()  # Rollback the transaction in case of any error
    finally:
        # Ensure the database connection is closed
        CONN.close()
        ###################################################################
def delete_borrowed_record(borrowed_book_id):
    CURSOR.execute("""
        DELETE FROM BorrowedBooks WHERE id = ?
    """, (borrowed_book_id,))
    
    CONN.commit()
    print(f"Borrowed book record with ID {borrowed_book_id} was deleted.")
    CONN.close()

    ###################################################################
def view_all_borrowed_books():
    CURSOR.execute("""
        SELECT BorrowedBooks.id, Users.name, Books.title, BorrowedBooks.borrow_date, BorrowedBooks.return_date, BorrowedBooks.returned
        FROM BorrowedBooks
        JOIN Users ON BorrowedBooks.user_id = Users.id
        JOIN Books ON BorrowedBooks.book_id = Books.id
    """)
    borrowed_books = CURSOR.fetchall()
    
    for book in borrowed_books:
        print(f"BorrowedBook ID: {book[0]}, User: {book[1]}, Book: {book[2]}, Borrow Date: {book[3]}, Return Date: {book[4]}, Returned: {book[5]}")
    CONN.commit()
    CONN.close()
    ###################################################################

def insert_borrowed_record(book_id, user_id, borrow_date, return_date=None, returned=False):
    """
    Inserts a new record into the BorrowedBooks table.
    """
    try:
        # Insert the new borrowed book record
        CURSOR.execute("""
            INSERT INTO BorrowedBooks (book_id, user_id, borrow_date, return_date, returned)
            VALUES (?, ?, ?, ?, ?)
        """, (book_id, user_id, borrow_date, return_date, returned))
        
        # Commit the transaction
        CONN.commit()
        print(f"Borrowed book record for book ID {book_id} and user ID {user_id} added successfully.")
    
    except Exception as e:
        print(f"An error occurred while inserting the borrowed book record: {e}")
        CONN.rollback()
    
    finally:
        CONN.close()

# Data for 5 borrowed books
borrowed_books_data = [
    (1, 101, '2023-08-01', None, False),  # Book ID 1 borrowed by User 101 on Aug 1, 2023
    (2, 102, '2023-08-05', None, False),  # Book ID 2 borrowed by User 102 on Aug 5, 2023
    (3, 103, '2023-08-10', None, False),  # Book ID 3 borrowed by User 103 on Aug 10, 2023
    (4, 104, '2023-08-12', None, False),  # Book ID 4 borrowed by User 104 on Aug 12, 2023
    (5, 105, '2023-08-15', None, False)   # Book ID 5 borrowed by User 105 on Aug 15, 2023
]

# Insert multiple records into the BorrowedBooks table
for BorrowedBooks in borrowed_books_data:
    insert_borrowed_record(*BorrowedBooks)


