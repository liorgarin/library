import sqlite3

class Customer:
    def __init__(self, customer_id, name, city, age):
        self.customer_id = customer_id
        self.name = name
        self.city = city
        self.age = age

    @staticmethod
    def add_customer(customer):
        conn = sqlite3.connect('library.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO Customers (Name, City, Age) VALUES (?, ?, ?)',
                       (customer.name, customer.city, customer.age))
        conn.commit()
        conn.close()

    @staticmethod
    def get_all_customers():
        conn = sqlite3.connect('library.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM Customers')
        customers = cursor.fetchall()
        conn.close()
        return customers

    @staticmethod
    def find_customer_by_name(name):
        conn = sqlite3.connect('library.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM Customers WHERE Name = ?', (name,))
        customer = cursor.fetchone()
        conn.close()
        return customer

    @staticmethod
    def remove_customer(customer_id):
        conn = sqlite3.connect('library.db')
        cursor = conn.cursor()
        cursor.execute('DELETE FROM Customers WHERE Id = ?', (customer_id,))
        conn.commit()
        conn.close()
