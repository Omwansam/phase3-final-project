from __init__ import CURSOR, CONN
from datetime import datetime, date



def create_issue_table():
    CURSOR.execute("""
        CREATE TABLE IF NOT EXISTS issue (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            book_id INTEGER,
            user_id INTEGER,
            borrow_date DATE,
            return_date DATE,
            FOREIGN KEY (book_id) REFERENCES books(id)
        )
    """)
    CONN.commit()
    print('Issue table was added successfully.')
    CONN.close()
    
  ###########################################################################

def issue_book():
    try:
        book_id = int(input("Enter the ID of the book to issue: "))
        CURSOR.execute("SELECT * FROM books WHERE id=?", (book_id,))
        book = CURSOR.fetchone()
        ...
        user_id = int(input("Enter your user ID: "))
        ...
        CONN.commit()
        print(f'Book "{book[1]}" has been issued successfully to user ID {user_id}.')
    except ValueError:
        print("Invalid input. Please enter valid IDs.")
    except Exception as e:
        print(f"An error occurred while issuing the book: {e}")
        CONN.rollback()
    finally:
        CONN.close()


        ##########################################################################

        #display issued book information
def display_issued_books():
            CURSOR.execute("SELECT * FROM issue WHERE return_date IS NULL")
            issues = CURSOR.fetchall()

            if issues:
                print("\nIssued Books:")
                print("ID | Book ID | User ID | Borrow Date | Return Date")
                for issue in issues:
                    print(f"{issue[0]} | {issue[1]} | {issue[2]} | {issue[3]} | {issue[4]}")
            else:
                print("\nNo issued books found.")
                return
            CONN.commit
            CONN.close()
#############################################################################################            

def return_book():
    try:
        book_id = int(input("Enter the ID of the book to return: "))
        user_id = int(input("Enter your user ID: "))

        CURSOR.execute("SELECT * FROM issue WHERE book_id=? AND user_id=? AND return_date IS NULL", (book_id, user_id))
        issue= CURSOR.fetchone()

        if issue is None:
            print("This book was not borrowed by you or has already been returned.")
            return

        # Update the return date
        CURSOR.execute("""
            UPDATE issues
            SET return_date = date('now')
            WHERE id = ?
        """, (issue[0],))  # transaction[0] is the transaction ID

        # Update the book's availability
        CURSOR.execute("""
            UPDATE books
            SET available = TRUE
            WHERE id = ?
        """, (book_id,))

        CONN.commit()
        print(f'Book "{book_id}" has been returned successfully.')

    except ValueError:
        print("Invalid input. Please enter valid IDs.")
    except Exception as e:
        print(f"An error occurred while returning the book: {e}")
        CONN.rollback()
    finally:
        CONN.close()







  