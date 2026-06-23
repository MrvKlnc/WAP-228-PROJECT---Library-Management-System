# WAP-228-PROJECT---Library-Management-System

This project is a Command Line Interface (CLI) application built with **Python** and **SQLite**. It serves as a Library Management System supporting standard CRUD (Create, Read, Update, Delete) operations for books, members, and borrowing records. 

## 🚀 Features

* **Books Management:** Add new books and view the complete list of books.
* **Smart Sorting:** * View books sorted alphabetically (A-Z) by **Title**.
* View books sorted alphabetically (A-Z) by **Author**.
* View members sorted alphabetically (A-Z) by **Name**.
* **Members Management:** Register new library members.
* **Borrowing System:** Link members to books. The system automatically updates the book's status to 'Borrowed'.
* **Returns:** Process book returns and update the system's availability status automatically.
* **Automated Unit Testing:** Includes 5 robust test cases for core operations and sorting logic using Python's built-in `unittest` framework.

## 🛠️ Technology Stack & Database Choice

* **Language:** Python 3.x
* **Database:** SQLite3
* **Version Control:** Git & GitHub

**Why SQLite? (Plug & Play Architecture)**
To ensure a smooth evaluation process, this project utilizes SQLite. This architectural choice eliminates the need for the evaluator to install, configure, or run external database servers (like MySQL or XAMPP). The application is entirely self-contained. Upon running the program, the relational SQL database (`library.db`) is automatically generated, providing a seamless "plug and play" experience while fully executing standard SQL queries.

## ⚙️ Prerequisites

* Python 3.x installed on your machine.
* No external third-party libraries are required. The project relies entirely on Python's standard libraries (`sqlite3`, `unittest`, `os`).

## 🖥️ How to Run the Project

Clone the repository to your local machine:
```bash
git clone https://github.com/MrvKlnc/WAP-228-PROJECT---Library-Management-System.git
```

Navigate into the project directory:
```bash
cd WAP-228-PROJECT---Library-Management-System
```

Run the application:
```bash
python main.py
```

(Note: Running `main.py` will automatically initialize the SQL database and create the necessary tables).

🧪 How to Run the Tests
To verify the integrity of the database queries and CRUD operations, run the test file. The tests use a temporary physical database (test_library.db) to avoid modifying the actual records and clean up after themselves automatically.

```bash
python -m unittest test_app.py
```

(Expected output: Ran 5 tests in ... OK)

🗄️ Database Schema
The project utilizes a relational SQL database with 3 tables:

1-books

-id (INTEGER, Primary Key)

-title (TEXT)

-author (TEXT)

-is_borrowed (INTEGER, Default 0)

2-members

-id (INTEGER, Primary Key)

-name (TEXT)

-email (TEXT, Unique)

3-borrow_records

-id (INTEGER, Primary Key)

-book_id (INTEGER, Foreign Key -> books.id)

-member_id (INTEGER, Foreign Key -> members.id)

-borrow_date (DATE)

-return_date (DATE)

👨‍💻 Author

Merve Kılınç - 240201458

GitHub:[@MrvKlnc] https://github.com/MrvKlnc

LinkedIn:[Merve Kılınç] https://www.linkedin.com/in/mrvkilincc/
