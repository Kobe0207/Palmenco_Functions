def display_menu():
    """Displays the food menu with prices."""
    menu = {
        "Burger": 5.50,
        "Pizza": 8.00,
        "Pasta": 6.75,
        "Salad": 4.25,
        "Soda": 1.50
    }
    
    print("Welcome to the Food Ordering System!")
    print("Menu:")
    for item, price in menu.items():
        print(f"{item}: ${price:.2f}")
    
    return menu

def get_order(menu):
    """Prompts the user to select a food item from the menu."""
    while True:
        choice = input("Please enter the food item you want to order: ").capitalize()
        if choice in menu:
            return choice, menu[choice]
        else:
            print("Invalid choice, please select a valid item from the menu.")

def process_payment(total):
    """Processes the payment and checks if the cash provided is sufficient."""
    while True:
        try:
            cash = float(input(f"Total: ${total:.2f}. Please enter the cash amount: $"))
            if cash >= total:
                change = cash - total
                return change
            else:
                print(f"Insufficient funds. You need ${total - cash:.2f} more.")
        except ValueError:
            print("Invalid input. Please enter a valid amount.")

def main():
    menu = display_menu()
    item, price = get_order(menu)
    print(f"You've selected {item} which costs ${price:.2f}.")
    
    change = process_payment(price)
    
    print(f"Payment successful! Your change is: ${change:.2f}")
    print("Thank you for your order!")

if __name__ == "__main__":
    main()
