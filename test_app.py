import unittest
import os
import main
import database

TEST_DB = "test_library.db"

class TestLibrarySystem(unittest.TestCase):

    def setUp(self):
        # Override the database name to use a temporary physical test database
        main.DB_NAME = TEST_DB
        database.init_db(TEST_DB)

    def tearDown(self):
        # Clean up (delete) the test database file after each test finishes
        if os.path.exists(TEST_DB):
            os.remove(TEST_DB)

    def test_add_book(self):
        main.add_book("1984", "George Orwell")
        books = main.fetch_query("SELECT * FROM books")
        self.assertEqual(len(books), 1)
        self.assertEqual(books[0][1], "1984")

    def test_add_member(self):
        main.add_member("John Doe", "john@example.com")
        members = main.fetch_query("SELECT * FROM members")
        self.assertEqual(len(members), 1)
        self.assertEqual(members[0][1], "John Doe")

    def test_borrow_book(self):
        # Setup: Add book and member
        main.add_book("The Hobbit", "J.R.R. Tolkien")
        main.add_member("Alice", "alice@example.com")
        
        # Action: Borrow book
        main.borrow_book(1, 1)
        
        # Assert: Check if book is marked as borrowed
        book_status = main.fetch_query("SELECT is_borrowed FROM books WHERE id = 1")[0][0]
        self.assertEqual(book_status, 1)

    # --- NEW: Tests for Alphabetical Sorting ---

    def test_sorting_books(self):
        # Setup: Add books out of alphabetical order
        main.add_book("Zebra", "Author B")
        main.add_book("Apple", "Author A")
        
        # Assert Title Sorting
        books_by_title = main.fetch_query("SELECT * FROM books ORDER BY title ASC")
        self.assertEqual(books_by_title[0][1], "Apple") # 'Apple' should be first
        
        # Assert Author Sorting
        books_by_author = main.fetch_query("SELECT * FROM books ORDER BY author ASC, title ASC")
        self.assertEqual(books_by_author[0][2], "Author A") # 'Author A' should be first

    def test_sorting_members(self):
        # Setup: Add members out of alphabetical order
        main.add_member("Zack", "zack@example.com")
        main.add_member("Alice", "alice@example.com")
        
        # Assert Member Name Sorting
        members = main.fetch_query("SELECT * FROM members ORDER BY name ASC")
        self.assertEqual(members[0][1], "Alice") # 'Alice' should be first

if __name__ == '__main__':
    unittest.main()