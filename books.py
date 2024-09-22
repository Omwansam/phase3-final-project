import sqlite3

def add_book():
    CONN = sqlite3.connect('/absolute/path/to/bookstores.db')
    CURSOR = CONN.cursor()
    CURSOR.execute("""    
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY,
            title TEXT NOT NULL,
            author TEXT NOT NULL,
            publication_date DATE,
            genre TEXT,
            available BOOLEAN DEFAULT TRUE
        )
    """)
    add_book()
    CONN.commit()
    print('Books table was added successfully')
    CONN.close()

def authenticate_librarians():
    name = input("Enter your name:.........")
    print(f"Welcome {name}")
    password = input("Enter your password:........")
    
    if password != "Admin":
        print("Invalid password. Access denied.")
        return None
    return name

def administrator_menu():
    name = authenticate_librarians()
    if name:
        while True:
            print("1. Add a book")
            print("2. Display all books")
            print("3. Delete a book")
            print("4. Update a book")
            print("5. Exit")
            choice = int(input("Enter your choice: "))

            if choice == 1:
                add_book()
            elif choice == 2:
                display_books()
            elif choice == 3:
                id = int(input("Enter the ID of the book to delete: "))
                delete_book(id)
            elif choice == 4:
                update_book()
            elif choice == 5:
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please try again.")

def insert_book(id, title, author, publication_date, genre, available):
    CONN = sqlite3.connect('bookstore.db')
    CURSOR = CONN.cursor()
    CURSOR.execute("""
        INSERT INTO books (id, title, author, publication_date, genre, available)
        VALUES (?, ?, ?, ?, ?, ?)""",
        (id, title, author, publication_date, genre, available))
    CONN.commit()
    print(f'Book with ID {id} was added successfully')  
    CONN.close()

def populate_books():
    CONN = sqlite3.connect('bookstore.db')
    CURSOR = CONN.cursor()
    CURSOR.execute('SELECT COUNT(*) FROM books')
    count = CURSOR.fetchone()[0]

    if count == 0:
        books_data = [
            (1, 'The Great Gatsby', 'F. Scott Fitzgerald', '1925-04-10', 'Novel', True),
            (2, '1984', 'George Orwell', '1949-06-08', 'Dystopian', True),
            (3, 'To Kill a Mockingbird', 'Harper Lee', '1960-07-11', 'Fiction', True),
            (4, 'Pride and Prejudice', 'Jane Austen', '1813-01-28', 'Romance', True),
            (5, 'Moby-Dick', 'Herman Melville', '1851-10-18', 'Adventure', False),
            (6, 'War and Peace', 'Leo Tolstoy', '1869-01-01', 'Historical Fiction', True),
            (7, 'The Catcher in the Rye', 'J.D. Salinger', '1951-07-16', 'Novel', False),
            (8, 'The Hobbit', 'J.R.R. Tolkien', '1937-09-21', 'Fantasy', True),
            (9, 'Brave New World', 'Aldous Huxley', '1932-08-18', 'Dystopian', True),
            (10, 'Frankenstein', 'Mary Shelley', '1818-01-01', 'Gothic Fiction', True)
        ]
        for book in books_data:
            insert_book(*book)
        print('Books data was inserted successfully')
    else:
        print('Books are already inserted')
    
    CONN.close()

def display_books():
    CONN = sqlite3.connect('bookstore.db')
    CURSOR = CONN.cursor()
    CURSOR.execute('SELECT * FROM books')
    books = CURSOR.fetchall()
    
    if not books:
        print("No books found.")
    else:
        for book in books:
            print(f'ID: {book[0]}, Title: {book[1]}, Author: {book[2]}, Publication Date: {book[3]}, Genre: {book[4]}, Available: {book[5]}')
    
    CONN.close()

def update_book():
    CONN = sqlite3.connect('bookstore.db')
    CURSOR = CONN.cursor()
    
    try:
        id = int(input("Enter the ID of the book to update: "))
        CURSOR.execute("SELECT * FROM books WHERE id=?", (id,))
        book = CURSOR.fetchone()

        if book is None:
            print(f"Book with ID {id} does not exist.")
            return

        new_title = input(f"Enter new title (current: {book[1]}): ") or book[1]
        new_author = input(f"Enter new author (current: {book[2]}): ") or book[2]
        new_publication_date = input(f"Enter new publication date (current: {book[3]}): ") or book[3]
        new_genre = input(f"Enter new genre (current: {book[4]}): ") or book[4]
        new_available = input(f"Is the book available (True/False) (current: {book[5]}): ")

        if new_available.lower() in ['true', 'false']:
            new_available = new_available.lower() == 'true'
        else:
            new_available = book[5]

        CURSOR.execute("""
            UPDATE books
            SET title = ?, author = ?, publication_date = ?, genre = ?, available = ?
            WHERE id = ?
        """, (new_title, new_author, new_publication_date, new_genre, new_available, id))

        CONN.commit()
        print(f'Book with ID {id} has been updated successfully.')

    except ValueError:
        print("Invalid input. Please enter a valid book ID.")
    
    except Exception as e:
        print(f"An error occurred while updating the book: {e}")
        CONN.rollback()

    finally:
        CONN.close()

def delete_book(id):
    CONN = sqlite3.connect('bookstore.db')
    CURSOR = CONN.cursor()

    try:
        CURSOR.execute("SELECT * FROM books WHERE id=?", (id,))
        book = CURSOR.fetchone()

        if book is None:
            print(f"Book with ID {id} does not exist.")
            return
        
        CURSOR.execute("DELETE FROM books WHERE id=?", (id,))
        CONN.commit()
        print(f'Book with ID {id} was deleted successfully.')

    except Exception as e:
        print(f"An error occurred while deleting the book: {e}")
        CONN.rollback()

    finally:
        CONN.close()

#if __name__ == '__main__':
        
    #add_book()  # Call this to create the table initially
   # populate_books()  # Populate the database with sample data
    #administrator_menu()  # Start the administrator menu
