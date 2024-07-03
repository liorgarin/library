# Library Management System

This project is a simple system to manage a book library, implemented in Python using SQLite.

## Project Structure

- `create_database.py`: Script to create the SQLite database and the required tables.
- `book.py`: Book class for managing operations on the Books table.
- `customer.py`: Customer class for managing operations on the Customers table.
- `loan.py`: Loan class for managing operations on the Loans table.
- `client.py`: Client application with a menu to perform various operations.
- `test_book.py`: Unit tests for the Book class.
- `test_customer.py`: Unit tests for the Customer class.
- `test_loan.py`: Unit tests for the Loan class.

## Requirements

- Python 3.x
- SQLite3

## Installation

1. Clone the repository or download the zip file and extract it.
2. Ensure you have Python 3.x installed.
3. Install SQLite3 if it is not already installed.

## Usage

1. **Create the Database**:
   Run `create_database.py` to create the SQLite database and the required tables.

   ```bash
   python create_database.py

## Run the Client Application:
**Run client.py to start the client application and interact with the menu options.**

python client.py

## Run Unit Tests:
**Run the unit tests to ensure everything is working correctly.**

python -m unittest test_book.py
python -m unittest test_customer.py
python -m unittest test_loan.py



