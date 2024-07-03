import unittest
from book import Book

class TestBook(unittest.TestCase):
    def test_add_and_remove_book(self):
        book = Book(None, 'Test Book', 'Test Author', 2024, 1)
        Book.add_book(book)
        fetched_book = Book.find_book_by_name('Test Book')
        self.assertIsNotNone(fetched_book)
        Book.remove_book(fetched_book[0])
        fetched_book = Book.find_book_by_name('Test Book')
        self.assertIsNone(fetched_book)

if __name__ == '__main__':
    unittest.main()
