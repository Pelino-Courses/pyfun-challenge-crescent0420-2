"""

Demonstrates the usage of the Product class: restocking, selling, and checking stock value.

Example:
    python inventory_demo.py
"""

from product import Product

def demo_product_operations():
    """
    Demonstrates product creation, restocking, selling, and getting stock value.
    """
    try:
        # Create a product
        laptop = Product("Laptop", 999.99, 10)
        print(laptop)

        # Restock the product
        laptop.restock(5)
        print("After restocking:", laptop)

        # Sell the product
        laptop.sell(3)
        print("After selling:", laptop)

        # Get stock value
        print("Stock value:", laptop.get_stock_value())

        # Handle invalid operations
        try:
            laptop.sell(20)  # Insufficient stock
        except ValueError as e:
            print(f"Error: {e}")

        try:
            laptop.restock(-5)  # Invalid amount
        except ValueError as e:
            print(f"Error: {e}")

    except ValueError as e:
        print(f"Error: {e}")

# Run the demo
if __name__ == "_main_":
    demo_product_operations()