import unittest
from coffee import Coffee
from customer import Customer

class TestCoffee(unittest.TestCase):

    def test_name_validation(self):
        with self.assertRaises(ValueError):
            Coffee("AB")  
        c = Coffee("Latte")
        self.assertEqual(c.name, "Latte")

    def test_orders_and_customers(self):
        coffee = Coffee("Espresso")
        alice = Customer("Alice")
        bob = Customer("Bob")
        
        alice.create_order(coffee, 4.0)
        bob.create_order(coffee, 5.0)

        self.assertEqual(len(coffee.orders()), 2)
        self.assertIn(alice, coffee.customers())
        self.assertIn(bob, coffee.customers())

    def test_num_orders_and_average_price(self):
        coffee = Coffee("Americano")
        self.assertEqual(coffee.num_orders(), 0)
        self.assertEqual(coffee.average_price(), 0)

        cust = Customer("Joe")
        cust.create_order(coffee, 3.0)
        cust.create_order(coffee, 6.0)

        self.assertEqual(coffee.num_orders(), 2)
        self.assertEqual(coffee.average_price(), 4.5)

if __name__ == '__main__':
    unittest.main()
