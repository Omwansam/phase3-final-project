from rich.console import Console
console = Console()


def main():
    print("""
        LIBRARY MANAGEMENT SYSTEM 
        
        1. ADD BOOK
        2. ISSUE OF BOOK
        3. RETURN OF BOOK
        4. DISPLAY BOOKS
        5. REPORT MENU
        6. EXIT PROGRAM    
        
        """)
    
    choice = input("Enter your choice (1-7):...... ")
    print('\n\n\n\n\n\n\n')
    if (choice == '1'):
        add_book()
    elif (choice == '2'):
        issue_book()  
    elif (choice == '3'):
        return_book()
    elif (choice == '4'):
        display_books()
    elif (choice == '5'):
        report_menu()
    elif (choice == '6'):    
        print(''' REPORT MENU 
            1. ISSUED BOOKS
            2. RETURNED BOOKS
            3. OVERDUE BOOKS
            4.GO BACK TO MAIN MENU
            \n\n\n  
            ''')
        
choice = input("Enter your choice (1-4): ")
print('\n\n\n\n\n\n\n')

if choice == '1':
    report_issued_books()
elif choice == '2':
    report_returned_books()
elif choice == '3':
    report_overdue_books()
elif choice == '4':
    main()   # main is defned earlier n the code 
elif choice == '7':
    print("Thank you for using the Library Management System. Goodbye!")
else:
    print("Invalid choice. Please try again.\n\n")
    main() # it loops back to the main function in case of an invalid choice
    
    if __name__ == '__main__':
        main() #Ensure the man function is called at the start of the program
