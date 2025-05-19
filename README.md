# ☕ Coffee Shop Challenge

This is a Python-based object-oriented programming (OOP) challenge that models a simple coffee shop domain using three main classes: `Customer`, `Coffee`, and `Order`.

## 🧠 Project Summary

- A `Customer` can place multiple `Orders`.
- An `Order` links a `Customer` to a `Coffee`.
- A `Coffee` can have multiple `Orders` from various `Customers`.

This models a **many-to-many** relationship between `Customer` and `Coffee` via `Order`.

## 📁 Folder Structure


## 🧪 Features

### ✅ Models

- `Customer(name)`
  - Name must be a string (1–15 chars)
  - Can create orders

- `Coffee(name)`
  - Name must be at least 3 characters
  - Name is immutable after creation

- `Order(customer, coffee, price)`
  - Price must be a float between 1.0–10.0
  - Links a customer and a coffee

### 🔁 Object Relationships

- `Customer.orders()` – All orders for the customer
- `Customer.coffees()` – Unique coffees the customer has ordered
- `Coffee.orders()` – All orders for the coffee
- `Coffee.customers()` – Unique customers who have ordered it

### 📊 Aggregations

- `Customer.create_order(coffee, price)`
- `Coffee.num_orders()` – Total number of orders
- `Coffee.average_price()` – Average order price
- `Customer.most_aficionado(coffee)` – Customer who spent the most on a given coffee

## 🧪 Running the Project

### Set up your environment:

```bash
pipenv install
pipenv shell
