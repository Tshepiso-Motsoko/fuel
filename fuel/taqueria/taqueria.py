MENU = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

def calculate_total(order):
    total = 0

    # Iterate over each item in the order
    for item in order:
        # Check if the item is in the menu
        if item in MENU:
            # Add the price of the item to the total
            total += MENU[item]

    return total


def main():
    order = []

    try:
        while True:
            # Prompt the user for an item
            item = input("Enter an item: ")

            # Convert the item to title case for case insensitivity
            item = item.title()

            if item not in MENU:
                # Invalid item, reprompt the user
                print("Invalid item. Please try again.")
            else:
                # Add the item to the order
                order.append(item)

                # Calculate the total and display it formatted as a dollar amount
                total = calculate_total(order)
                print(f"Total: ${total:.2f}")

    except EOFError:
        # User input ended, exit the program
        pass


if __name__ == "__main__":
    main()
