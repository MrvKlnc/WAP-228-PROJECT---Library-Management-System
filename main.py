import sqlite3
from database import init_db

DB_NAME = "library.db"

def execute_query(query, parameters=()):
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute(query, parameters)
        conn.commit()
        return cursor

def fetch_query(query, parameters=()):
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute(query, parameters)
        return cursor.fetchall()

# --- CRUD OPERATIONS ---

def add_book(title, author):
    execute_query("INSERT INTO books (title, author) VALUES (?, ?)", (title, author))
    print(f"Success: Book '{title}' added.")

def view_books():
    # Fetch books sorted alphabetically by title (A-Z)
    books = fetch_query("SELECT * FROM books ORDER BY title ASC")
    print("\n--- Book List (Sorted by Title) ---")
    for book in books:
        status = "Borrowed" if book[3] == 1 else "Available"
        print(f"ID: {book[0]} | Title: {book[1]} | Author: {book[2]} | Status: {status}")
    print("-----------------------------------\n")

def view_books_by_author():
    # Fetch books sorted alphabetically by author, then by title (A-Z)
    books = fetch_query("SELECT * FROM books ORDER BY author ASC, title ASC")
    print("\n--- Book List (Sorted by Author) ---")
    for book in books:
        status = "Borrowed" if book[3] == 1 else "Available"
        print(f"ID: {book[0]} | Title: {book[1]} | Author: {book[2]} | Status: {status}")
    print("------------------------------------\n")

def add_member(name, email):
    try:
        execute_query("INSERT INTO members (name, email) VALUES (?, ?)", (name, email))
        print(f"Success: Member '{name}' added.")
    except sqlite3.IntegrityError:
        print("Error: A member with this email already exists.")

def view_members_by_name():
    # Fetch members sorted alphabetically by name (A-Z)
    members = fetch_query("SELECT * FROM members ORDER BY name ASC")
    print("\n--- Member List (Sorted by Name) ---")
    for member in members:
        print(f"ID: {member[0]} | Name: {member[1]} | Email: {member[2]}")
    print("------------------------------------\n")

def borrow_book(book_id, member_id):
    # Check if book exists and is available
    book = fetch_query("SELECT is_borrowed FROM books WHERE id = ?", (book_id,))
    if not book:
        print("Error: Book not found.")
        return
    if book[0][0] == 1:
        print("Error: Book is already borrowed.")
        return
    
    # Update book status and create record
    execute_query("UPDATE books SET is_borrowed = 1 WHERE id = ?", (book_id,))
    execute_query("INSERT INTO borrow_records (book_id, member_id) VALUES (?, ?)", (book_id, member_id))
    print("Success: Book borrowed successfully.")

def return_book(book_id):
    # Update book status and set return date
    execute_query("UPDATE books SET is_borrowed = 0 WHERE id = ?", (book_id,))
    
    # Split query to avoid E501 (Line too long) PEP 8 warning
    query = (
        "UPDATE borrow_records SET return_date = date('now') "
        "WHERE book_id = ? AND return_date IS NULL"
    )
    execute_query(query, (book_id,))
    
    print("Success: Book returned successfully.")

# --- CLI MENU ---

def main():
    init_db() # Ensure DB is ready
    while True:
        print("\n=== Library Management System ===")
        print("1. Add a New Book")
        print("2. View All Books (A-Z by Title)")
        print("3. View Books (A-Z by Author)")
        print("4. Add a New Member")
        print("5. View Members (A-Z by Name)")
        print("6. Borrow a Book")
        print("7. Return a Book")
        print("8. Exit")
        
        choice = input("Enter your choice (1-8): ")
        
        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            add_book(title, author)
        elif choice == '2':
            view_books()
        elif choice == '3':
            view_books_by_author()
        elif choice == '4':
            name = input("Enter member name: ")
            email = input("Enter member email: ")
            add_member(name, email)
        elif choice == '5':
            view_members_by_name()
        elif choice == '6':
            book_id = input("Enter Book ID: ")
            member_id = input("Enter Member ID: ")
            borrow_book(book_id, member_id)
        elif choice == '7':
            book_id = input("Enter Book ID to return: ")
            return_book(book_id)
        elif choice == '8':
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
    