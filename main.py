from rich.console import Console
from books import administrator_menu

from books import display_books


console = Console()


def main():
    print("""
        LIBRARY MANAGEMENT SYSTEM 
        
        1. ADMINISTRATOR
        2. ISSUE OF BOOK
        3. RETURN OF BOOK
        4. DISPLAY BOOKS
        5. EXIT PROGRAM    
        
        """)
    
    choice = input("Enter your choice (1-7):...... ")
    print('\n\n\n\n\n\n\n')
    if (choice == '1'):
        administrator_menu()
    elif (choice == '2'):
        issue_book()
    elif (choice == '3'):
        return_book()
    elif (choice == '4'):
        display_books()
    elif choice == '5':
        print("Exiting the program. Goodbye!")
        return  # Exit the function (and program)
    else:
        print("Invalid choice. Please try again.\n")
        main()  # Loop back to the main function in case of an invalid choice

if __name__ == '__main__':
    main()  # Ensure the main function is called at the start of the program