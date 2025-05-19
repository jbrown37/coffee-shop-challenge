import unittest
from customer import Customer
from coffee import Coffee

class TestCustomer(unittest.TestCase):
    def test_name_validation(self):
        with self.assertRaises(ValueError):
            Customer("")  # Too short
        with self.assertRaises(ValueError):
            Customer("x" * 20)  # Too long

    def test_create_order(self):
        customer = Customer("Alice")
        coffee = Coffee("Latte")
        order = customer.create_order(coffee, 4.5)
        self.assertIn(order, customer.orders())
        self.assertIn(order, coffee.orders())
