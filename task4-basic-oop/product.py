"""
 Allows operations like restocking, selling, and calculating stock value.

Usage:
    product = Product("Laptop", 999.99, 10)
    product.restock(5)
    product.sell(3)
    print(product.get_stock_value())
"""

class Product:
    """
    Represents a product with attributes: name, price, and quantity.

    Methods:
        _init_(name, price, quantity) - Initializes a product with name, price, and quantity.
        restock(amount) - Increases stock by a given amount.
        sell(amount) - Sells the product, decreasing the stock.
        get_stock_value() - Returns the total value of stock.
        _str_() - String representation of the product.
    """

    def _init_(self, name: str, price: float, quantity: int):
        """
        Initializes a product with name, price, and quantity.

        Args:
            name (str): Product name.
            price (float): Product price.
            quantity (int): Product stock quantity.
        
        Raises:
            ValueError: If any input is invalid.
        """
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Product name must be a non-empty string.")
        if not isinstance(price, (int, float)) or price < 0:
            raise ValueError("Price must be non-negative.")
        if not isinstance(quantity, int) or quantity < 0:
            raise ValueError("Quantity must be non-negative.")

        self._name = name.strip()
        self._price = float(price)
        self._quantity = quantity

    @property
    def name(self):
        """Returns the product's name."""
        return self._name

    @property
    def price(self):
        """Returns the product's price."""
        return self._price

    @price.setter
    def price(self, new_price):
        """Sets the product's price."""
        if new_price < 0:
            raise ValueError("Price must be non-negative.")
        self._price = new_price

    @property
    def quantity(self):
        """Returns the product's stock quantity."""
        return self._quantity

    @quantity.setter
    def quantity(self, new_quantity):
        """Sets the product's stock quantity."""
        if new_quantity < 0:
            raise ValueError("Quantity must be non-negative.")
        self._quantity = new_quantity

    def restock(self, amount: int):
        """Increases stock by a given amount."""
        if amount <= 0:
            raise ValueError("Restock amount must be positive.")
        self._quantity += amount

    def sell(self, amount: int):
        """Sells the product, reducing stock by the given amount."""
        if amount <= 0:
            raise ValueError("Sell amount must be positive.")
        if amount > self._quantity:
            raise ValueError("Insufficient stock.")
        self._quantity -= amount

    def get_stock_value(self):
        """Returns the total value of the stock."""
        return self._price * self._quantity

    def _str_(self):
        """Returns a string representation of the product."""
        return f"Product(name='{self._name}', price=${self._price:.2f}, quantity={self._quantity})"