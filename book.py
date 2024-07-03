import sqlite3

class Book:
    def __init__(self, book_id, name, author, year_published, book_type):
        self.book_id = book_id
        self.name = name
        self.author = author
        self.year_published = year_published
        self.book_type = book_type

    @staticmethod
    def add_book(book):
        conn = sqlite3.connect('library.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO Books (Name, Author, YearPublished, Type) VALUES (?, ?, ?, ?)',
                       (book.name, book.author, book.year_published, book.book_type))
        conn.commit()
        conn.close()

    @staticmethod
    def get_all_books():
        conn = sqlite3.connect('library.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM Books')
        books = cursor.fetchall()
        conn.close()
        return books

    @staticmethod
    def find_book_by_name(name):
        conn = sqlite3.connect('library.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM Books WHERE Name = ?', (name,))
        book = cursor.fetchone()
        conn.close()
        return book

    @staticmethod
    def remove_book(book_id):
        conn = sqlite3.connect('library.db')
        cursor = conn.cursor()
        cursor.execute('DELETE FROM Books WHERE Id = ?', (book_id,))
        conn.commit()
        conn.close()
