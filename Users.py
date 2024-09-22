from __init__ import CURSOR, CONN

# Function to create the Users table
def create_users_table():
    CURSOR.execute("""
        CREATE TABLE IF NOT EXISTS Users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            phone TEXT,
            employee BOOLEAN DEFAULT FALSE
        )
    """)
    CONN.commit()
    print("Users table created successfully.")
    CONN.close()

    #############################################################################
    #Add users to the table
def add_user(name, email, phone, employee=False):
    CURSOR.execute("""
        INSERT INTO Users (name, email, phone, employee)
        VALUES (?, ?, ?, ?)
    """, (name, email, phone, employee))
    
    CONN.commit()
    print(f"User {name} added successfully.")
    CONN.close()
    ############################################################################
    # Function to retrieve all users from the table
    def get_all_users():
        CURSOR.execute("SELECT * FROM Users")
        return CURSOR.fetchall()
    
    # Function to retrieve a specific user by email
    def get_user_by_email(email):
        CURSOR.execute("SELECT * FROM Users WHERE email=?", (email,))
        return CURSOR.fetchone()
    
    # Function to update a user's information
    def update_user(id, name=None, email=None, phone=None, employee=None):
        updates = []
        values = []
        
        if name:
            updates.append("name=?")
            values.append(name)
        
        if email:
            updates.append("email=?")
            values.append(email)
        
        if phone:
            updates.append("phone=?")
            values.append(phone)
        
        if employee is not None:
            updates.append("employee=?")
            values.append(employee)

            CONN.commit()
            CONN.close()            

            #Function to delete user information
            def delete_user(id):
                CURSOR.execute("DELETE FROM Users WHERE id=?", (id,))
                CONN.commit()
                print(f"User with ID {id} deleted successfully.")
                CONN.close()





''''''def add_user(name, email, phone, employee=False):
    """
    Inserts a new user into the Users table.
    """
    try:
        CURSOR.execute("""
            INSERT INTO Users (name, email, phone, employee)
            VALUES (?, ?, ?, ?)
        """, (name, email, phone, employee))
        
        CONN.commit()
        print(f"User {name} added successfully.")
    
    except Exception as e:
        print(f"An error occurred while adding the user: {e}")
        CONN.rollback()
    
    finally:
        CONN.close()

# Data for 15 users
users_data = [
    ("Alice Johnson", "alice.johnson@example.com", "123-456-7890", True),
    ("Bob Smith", "bob.smith@example.com", "234-567-8901", True),
    ("Charlie Brown", "charlie.brown@example.com", "345-678-9012", False),
    ("David Wilson", "david.wilson@example.com", "456-789-0123", True),
    ("Eva Green", "eva.green@example.com", "567-890-1234", False),
    ("Frank Wright", "frank.wright@example.com", "678-901-2345", True),
    ("Grace Lee", "grace.lee@example.com", "789-012-3456", False),
    ("Henry Adams", "henry.adams@example.com", "890-123-4567", True),
    ("Ivy Carter", "ivy.carter@example.com", "901-234-5678", False),
    ("Jack Turner", "jack.turner@example.com", "012-345-6789", True),
    ("Kara Evans", "kara.evans@example.com", "123-456-7801", False),
    ("Leo Scott", "leo.scott@example.com", "234-567-8912", True),
    ("Mia Thompson", "mia.thompson@example.com", "345-678-9023", False),
    ("Nina Baker", "nina.baker@example.com", "456-789-0134", True),
    ("Owen Hall", "owen.hall@example.com", "567-890-1245", False),
    ("Paula Young", "paula.young@example.com", "678-901-2356", True)
]

# Insert multiple records into the Users table
for user in users_data:
    add_user(*user)
'''