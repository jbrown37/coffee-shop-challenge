
from customer import Customer
from coffee import Coffee
from order import Order

alice = Customer("Alice")
bob = Customer("Bob")

latte = Coffee("Latte")
espresso = Coffee("Espresso")

alice.create_order(latte, 4.5)
alice.create_order(espresso, 3.0)
bob.create_order(latte, 5.0)
bob.create_order(latte, 6.5)

print(f"{alice.name}'s orders:")
for order in alice.orders():
    print(f"- {order.coffee.name} at ${order.price:.2f}")

print(f"\nCoffees Alice has ordered:")
for coffee in alice.coffees():
    print(f"- {coffee.name}")

print(f"\nCustomers who ordered Latte:")
for customer in latte.customers():
    print(f"- {customer.name}")

print(f"\nTotal number of Latte orders: {latte.num_orders()}")
print(f"Average price of Latte orders: ${latte.average_price():.2f}")

from customer import Customer  # Ensure the classmethod is present
top_customer = Customer.most_aficionado(latte)
print(f"\nCustomer who spent the most on Latte: {top_customer.name}")
