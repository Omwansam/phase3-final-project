from __init__ import CURSOR, CONN
from tabulate import tabulate 

def authenticate_librarians():
    # Authenticate librarians

    name = input("Enter your name:.........")
    print(f"Welcome {name}")
    password = input("Enter your password:........")

    if password != "Admin":
        print("Invalid password. Access denied.")
        return None
    return name
##############################################################################

def administrator_menu():
    name = authenticate_librarians()
    if name:
        while True:
            print("1. Add a book")
            print("2. Display all books")
            print("3. Delete a book")
            print("4. Exit")
            choice = int(input("Enter"))

            if choice == 1:
                add_book()
            elif choice == 2:
                display_books()
            elif choice == 3:
                id = int(input("Enter the ID of the book to delete: "))
                delete_book(id)
            elif choice == 4:
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please try again.")

############################################################################33                

def display_books():
    CURSOR.execute("SELECT * FROM books")
    books = CURSOR.fetchall()

    if not books:
        print("No books found.")
    else:
        headers = ["ID", "Title", "Author", "Publication Date", "Genre", "Available"]
        # Ensure the columns align with what you are fetching from the table
        print(tabulate(books, headers=headers, tablefmt="grid"))
    
    CONN.close()  # Closing the connection after fetching the results

    ####################################################################

    def delete_book(id):
        # Delete a book
        CURSOR.execute("DELETE FROM books WHERE id=?", (id,))
        CONN.commit()
        print(f'Book with ID {id} was deleted successfully')
        CONN.close()

###############################################################################
def add_book():

    CURSOR.execute("""
            CREATE TABLE IF NOT EXISTS `books` (
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    author = Column(String, nullable=False)
    publication_date = Column(Date)
    genre = Column(String)
    available = Column(Boolean, default=True)
    transactions = relationship('Transaction', back_populates='book')
""")
    
    CONN.commit()
    print('Books table was added successfully')
    CONN.close()

    #################################################################################


    def insert_book(id, title, author, publication_date, genre, available, transactions):
        # Insert a new book
        CURSOR.execute("""
            INSERT INTO books (id, title, author, publication_date, genre, available, transactions)
            VALUES (?, ?, ?, ?, ?, ?, ?)""",
                    (id, title, author, publication_date, genre, available, transactions))
        CONN.commit()
        print(f'Book with ID {id} was added successfully')
        CONN.close()

        ##############################################################################
