class Customer:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Customer(name={self.name})"

class Coffee:
    def __init__(self, flavor):
        self.flavor = flavor

    def __repr__(self):
        return f"Coffee(flavor={self.flavor})"

class Order:
    all_orders = []  # Class-level list to store all orders

    def __init__(self, customer, coffee, price):
        if not isinstance(customer, Customer):
            raise ValueError("Customer must be an instance of Customer.")
        if not isinstance(coffee, Coffee):
            raise ValueError("Coffee must be an instance of Coffee.")
        if not isinstance(price, float) or not (1.0 <= price <= 10.0):
            raise ValueError("Price must be a float between 1.0 and 10.0.")
        
        self._customer = customer
        self._coffee = coffee
        self._price = price
        
        # Register this order with the Order class
        Order.all_orders.append(self)

    @property
    def customer(self):
        return self._customer

    @property
    def coffee(self):
        return self._coffee

    @property
    def price(self):
        return self._price

    def __repr__(self):
        return (f"Order(customer={self.customer}, coffee={self.coffee}, price={self.price:.2f})")

# Example usage
customer1 = Customer("Abdalla")
coffee1 = Coffee("cappucino")

# Create an order
order1 = Order(customer1, coffee1, 4.5)

# Check all orders
print(Order.all_orders)
