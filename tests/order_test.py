import unittest
from customer import Customer
from coffee import Coffee
from order import Order

class TestOrder(unittest.TestCase):

    def test_order_initialization(self):
        cust = Customer("Anna")
        coffee = Coffee("Mocha")
        order = Order(cust, coffee, 5.5)

        self.assertEqual(order.customer, cust)
        self.assertEqual(order.coffee, coffee)
        self.assertEqual(order.price, 5.5)

    def test_invalid_customer_type(self):
        with self.assertRaises(TypeError):
            Order("NotACustomer", Coffee("Latte"), 3.0)

    def test_invalid_coffee_type(self):
        with self.assertRaises(TypeError):
            Order(Customer("Dan"), "NotACoffee", 3.0)

    def test_invalid_price_type_or_range(self):
        cust = Customer("Rick")
        coffee = Coffee("Cappuccino")

        with self.assertRaises(ValueError):
            Order(cust, coffee, 0.5)  # too low

        with self.assertRaises(ValueError):
            Order(cust, coffee, 15.0)  # too high

        with self.assertRaises(ValueError):
            Order(cust, coffee, "not a float")

if __name__ == '__main__':
    unittest.main()
