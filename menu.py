menu = {
    "coffee": 150000,
    "tea": 80000,
    "cake": 200000
}


def show_menu():
    print("\n========== Cafe Menu ==========")

    for product, price in menu.items():
        print(f"{product}: {price:,} Toman")

if __name__ == "__main__":
    show_menu()