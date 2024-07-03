import sqlite3
from datetime import datetime, timedelta

class Loan:
    def __init__(self, cust_id, book_id, loan_date, return_date=None):
        self.cust_id = cust_id
        self.book_id = book_id
        self.loan_date = loan_date
        self.return_date = return_date

    @staticmethod
    def loan_book(loan):
        conn = sqlite3.connect('library.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO Loans (CustID, BookID, LoanDate) VALUES (?, ?, ?)',
                       (loan.cust_id, loan.book_id, loan.loan_date))
        conn.commit()
        conn.close()

    @staticmethod
    def return_book(cust_id, book_id):
        conn = sqlite3.connect('library.db')
        cursor = conn.cursor()
        return_date = datetime.now().strftime("%Y-%m-%d")
        cursor.execute('UPDATE Loans SET ReturnDate = ? WHERE CustID = ? AND BookID = ?',
                       (return_date, cust_id, book_id))
        conn.commit()
        conn.close()

    @staticmethod
    def get_all_loans():
        conn = sqlite3.connect('library.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM Loans')
        loans = cursor.fetchall()
        conn.close()
        return loans

    @staticmethod
    def get_late_loans():
        conn = sqlite3.connect('library.db')
        cursor = conn.cursor()
        today = datetime.now().strftime("%Y-%m-%d")
        cursor.execute('SELECT * FROM Loans WHERE ReturnDate IS NULL AND LoanDate < ?', (today,))
        late_loans = cursor.fetchall()
        conn.close()
        return late_loans
