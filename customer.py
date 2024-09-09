class Customer:
    def __init__(self, name):
        self._set_name(name)
        self._orders = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._set_name(value)

    def _set_name(self, value):
        if not isinstance(value, str) or len(value) < 1 or len(value) > 15:
            raise ValueError("Name must be a string between 1 and 15 characters.")
        self._name = value

    def orders(self):
        """Returns a list of all orders for this customer."""
        return self._orders

    def coffees(self):
        """Returns a unique list of all coffees ordered by this customer."""
        return list({order.coffee for order in self._orders})

    def create_order(self, coffee, price):
        """Creates and returns a new order instance for this customer."""
        order = Order(self, coffee, price)
        self._orders.append(order)
        return order
