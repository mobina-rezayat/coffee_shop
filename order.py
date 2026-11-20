from menu import menu

orders = []


def add_order():
    product = input("Enter product name: ").strip().lower()

    if product not in menu:
        print("Product not found in menu!")
        return

    try:
        quantity = int(input("Enter quantity: "))

        if quantity <= 0:
            print("Quantity must be greater than zero!")
            return

    except ValueError:
        print("Please enter a valid number!")
        return

    order = {
        "product": product,
        "price": menu[product],
        "quantity": quantity
    }

    orders.append(order)
    print("Order added successfully!")


def show_orders():
    if not orders:
        print("No orders registered yet!")
        return

    print("\n========== Orders ==========")

    for order in orders:
        print(
            f"Product: {order['product']} | "
            f"Price: {order['price']:,} | "
            f"Quantity: {order['quantity']}"
        )


if __name__ == "__main__":
    add_order()
    show_orders()