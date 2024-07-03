from book import Book
from customer import Customer
from loan import Loan
from datetime import datetime

def main_menu():
    while True:
        print("\nLibrary Management System")
        print("1. Add a new customer")
        print("2. Add a new book")
        print("3. Loan a book")
        print("4. Return a book")
        print("5. Display all books")
        print("6. Display all customers")
        print("7. Display all loans")
        print("8. Display late loans")
        print("9. Find book by name")
        print("10. Find customer by name")
        print("11. Remove book")
        print("12. Remove customer")
        print("13. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter customer name: ")
            city = input("Enter customer city: ")
            age = int(input("Enter customer age: "))
            customer = Customer(None, name, city, age)
            Customer.add_customer(customer)
            print("Customer added successfully.")
        elif choice == '2':
            name = input("Enter book name: ")
            author = input("Enter book author: ")
            year = int(input("Enter year published: "))
            book_type = int(input("Enter book type (1/2/3): "))
            book = Book(None, name, author, year, book_type)
            Book.add_book(book)
            print("Book added successfully.")
        elif choice == '3':
            cust_id = int(input("Enter customer ID: "))
            book_id = int(input("Enter book ID: "))
            loan_date = datetime.now().strftime("%Y-%m-%d")
            loan = Loan(cust_id, book_id, loan_date)
            Loan.loan_book(loan)
            print("Book loaned successfully.")
        elif choice == '4':
            cust_id = int(input("Enter customer ID: "))
            book_id = int(input("Enter book ID: "))
            Loan.return_book(cust_id, book_id)
            print("Book returned successfully.")
        elif choice == '5':
            books = Book.get_all_books()
            for book in books:
                print(book)
        elif choice == '6':
            customers = Customer.get_all_customers()
            for customer in customers:
                print(customer)
        elif choice == '7':
            loans = Loan.get_all_loans()
            for loan in loans:
                print(loan)
        elif choice == '8':
            late_loans = Loan.get_late_loans()
            for loan in late_loans:
                print(loan)
        elif choice == '9':
            name = input("Enter book name: ")
            book = Book.find_book_by_name(name)
            print(book)
        elif choice == '10':
            name = input("Enter customer name: ")
            customer = Customer.find_customer_by_name(name)
            print(customer)
        elif choice == '11':
            book_id = int(input("Enter book ID to remove: "))
            Book.remove_book(book_id)
            print("Book removed successfully.")
        elif choice == '12':
            customer_id = int(input("Enter customer ID to remove: "))
            Customer.remove_customer(customer_id)
            print("Customer removed successfully.")
        elif choice == '13':
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main_menu()
