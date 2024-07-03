import unittest
from customer import Customer

class TestCustomer(unittest.TestCase):
    def test_add_and_remove_customer(self):
        customer = Customer(None, 'Test Customer', 'Test City', 30)
        Customer.add_customer(customer)
        fetched_customer = Customer.find_customer_by_name('Test Customer')
        self.assertIsNotNone(fetched_customer)
        Customer.remove_customer(fetched_customer[0])
        fetched_customer = Customer.find_customer_by_name('Test Customer')
        self.assertIsNone(fetched_customer)

if __name__ == '__main__':
    unittest.main()
