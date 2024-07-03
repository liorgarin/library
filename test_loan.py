import unittest
from loan import Loan
from book import Book
from customer import Customer
from datetime import datetime

class TestLoan(unittest.TestCase):
    def test_loan_and_return_book(self):
        customer = Customer(None, 'Test Customer', 'Test City', 30)
        Customer.add_customer(customer)
        fetched_customer = Customer.find_customer_by_name('Test Customer')

        book = Book(None, 'Test Book', 'Test Author', 2024, 1)
        Book.add_book(book)
        fetched_book = Book.find_book_by_name('Test Book')

        loan = Loan(fetched_customer[0], fetched_book[0], datetime.now().strftime("%Y-%m-%d"))
        Loan.loan_book(loan)

        loans = Loan.get_all_loans()
        self.assertTrue(any(l[0] == fetched_customer[0] and l[1] == fetched_book[0] for l in loans))

        Loan.return_book(fetched_customer[0], fetched_book[0])

        loans = Loan.get_all_loans()
        self.assertTrue(any(l[0] == fetched_customer[0] and l[1] == fetched_book[0] and l[3] is not None for l in loans))

        Customer.remove_customer(fetched_customer[0])
        Book.remove_book(fetched_book[0])

if __name__ == '__main__':
    unittest.main()
