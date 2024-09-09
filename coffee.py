class Coffee:
    def __init__(self, name):
        self._set_name(name)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._set_name(value)

    def _set_name(self, value):
        if not isinstance(value, str) or len(value) < 3:
            raise ValueError("Name must be a string with at least 3 characters.")
        self._name = value

    def orders(self):
        """Returns a list of all orders for this coffee."""
        return [order for order in Order.all_orders if order.coffee == self]

    def customers(self):
        """Returns a unique list of all customers who have ordered this coffee."""
        return list({order.customer for order in self.orders()})

    def num_orders(self):
        """Returns the total number of orders for this coffee."""
        return len(self.orders())

    def average_price(self):
        """Returns the average price of this coffee based on its orders."""
        orders = self.orders()
        if not orders:
            return 0
        total_price = sum(order.price for order in orders)
        return total_price / len(orders)
