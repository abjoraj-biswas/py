import mysql.connector as a 

def connect_db():
    return a.connect(
        host="localhost",
        user="root",
        password="abjoraj2006",
        database="library_db",
        autocommit=True
    )

def create_tables():
    db = connect_db()
    cursor = db.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS books (
            id INT AUTO_INCREMENT PRIMARY KEY,
            title VARCHAR(255) NOT NULL,
            author VARCHAR(255) NOT NULL,
            available BOOLEAN DEFAULT TRUE )""")
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS transactions (
            id INT AUTO_INCREMENT PRIMARY KEY,
            book_id INT,
            issued_to VARCHAR(255),
            issue_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            return_date TIMESTAMP NULL,
            FOREIGN KEY (book_id) REFERENCES books(id))""")
 
    db.close()

def add_book(title, author):
    db = connect_db()
    cursor = db.cursor()
    cursor.execute("INSERT INTO books (title, author) VALUES (%s, %s)", (title, author))

    db.close()

def issue_book(book_id, issued_to):
    db = connect_db()
    cursor = db.cursor()
    cursor.execute("SELECT available FROM books WHERE id = %s", (book_id,))
    book = cursor.fetchone()
    if book and book[0]:
        cursor.execute("UPDATE books SET available = FALSE WHERE id = %s", (book_id,))
        cursor.execute("INSERT INTO transactions (book_id, issued_to) VALUES (%s, %s)", (book_id, issued_to))
 
        print("Book issued successfully.")
    else:
        print("Book not available.")
    db.close()

def return_book(book_id):
    db = connect_db()
    cursor = db.cursor()
    cursor.execute("UPDATE books SET available = TRUE WHERE id = %s", (book_id,))
    cursor.execute("UPDATE transactions SET return_date = NOW() WHERE book_id = %s AND return_date IS NULL", (book_id,))

    db.close()
    print("Book returned successfully.")

def view_books():
    db = connect_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM books")
    books = cursor.fetchall()
    for book in books:
        print(book)
    db.close()

if __name__ == "__main__":
    create_tables()
    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. Issue Book")
        print("3. Return Book")
        print("4. View Books")
        print("5. Exit")
        choice = input("Enter choice: ")
        if choice == "1":
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            add_book(title, author)
        elif choice == "2":
            book_id = int(input("Enter book ID to issue: "))
            issued_to = input("Enter issuer name: ")
            issue_book(book_id, issued_to)
        elif choice == "3":
            book_id = int(input("Enter book ID to return: "))
            return_book(book_id)
        elif choice == "4":
            view_books()
        elif choice == "5":
            break
        else:
            print("Invalid choice, try again.")
