import sqlite3

def create_tables():
    connection = sqlite3.connect('library.db')
    cursor = connection.cursor()

    # Create Books table
    cursor.execute('''CREATE TABLE IF NOT EXISTS Books (
                        Id INTEGER PRIMARY KEY,
                        Name TEXT NOT NULL,
                        Author TEXT NOT NULL,
                        YearPublished INTEGER NOT NULL,
                        Type INTEGER NOT NULL)''')

    # Create Customers table
    cursor.execute('''CREATE TABLE IF NOT EXISTS Customers (
                        Id INTEGER PRIMARY KEY,
                        Name TEXT NOT NULL,
                        City TEXT NOT NULL,
                        Age INTEGER NOT NULL)''')

    # Create Loans table
    cursor.execute('''CREATE TABLE IF NOT EXISTS Loans (
                        CustID INTEGER,
                        BookID INTEGER,
                        LoanDate TEXT NOT NULL,
                        ReturnDate TEXT,
                        FOREIGN KEY (CustID) REFERENCES Customers(Id),
                        FOREIGN KEY (BookID) REFERENCES Books(Id))''')

    connection.commit()
    connection.close()

if __name__ == "__main__":
    create_tables()
