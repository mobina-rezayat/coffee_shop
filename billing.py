from order import orders


def calculate_total():
    total = 0

    for order in orders:
        total += order["price"] * order["quantity"]

    return total


def calculate_discount(total):
    if total > 1000000:
        discount = total * 0.10
    else:
        discount = 0

    return discount


def print_invoice():
    if not orders:
        print("No orders to invoice!")
        return

    print("\n========== Invoice ==========")

    for order in orders:
        product = order["product"]
        quantity = order["quantity"]
        price = order["price"]

        print(f"{product} | Quantity: {quantity} | Price: {price:,}")

    total = calculate_total()
    discount = calculate_discount(total)
    final_amount = total - discount

    print("=============================")
    print(f"Total: {total:,} Toman")
    print(f"Discount: {discount:,.0f} Toman")
    print(f"Final Amount: {final_amount:,.0f} Toman")