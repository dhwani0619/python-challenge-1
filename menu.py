# Menu dictionary
menu = {
    "1. Snacks": {
        "Cookie": .99,
        "Banana": .69,
        "Apple": .49,
        "Granola bar": 1.99
    },
    "2. Meals": {
        "Burrito": 4.49,
        "Teriyaki Chicken": 9.99,
        "Sushi": 7.49,
        "Pad Thai": 6.99,
        "Pizza": {
            "Cheese": 8.99,
            "Pepperoni": 10.99,
            "Vegetarian": 9.99
        },
        "Burger": {
            "Chicken": 7.49,
            "Beef": 8.49
        }
    },
    "3. Drinks": {
        "Soda": {
            "Small": 1.99,
            "Medium": 2.49,
            "Large": 2.99
        },
        "Tea": {
            "Green": 2.49,
            "Thai iced": 3.99,
            "Irish breakfast": 2.49
        },
        "Coffee": {
            "Espresso": 2.99,
            "Flat white": 2.99,
            "Iced": 3.49
        }
    },
    "4. Dessert": {
        "Chocolate lava cake": 10.99,
        "Cheesecake": {
            "New York": 4.99,
            "Strawberry": 6.49
        },
        "Australian Pavlova": 9.99,
        "Rice pudding": 4.99,
        "Fried banana": 4.49
    }
}

# Empty order list 
order_list = []


# Displaying the Menu
def display_menu():
    print ("Welcome to the Variety Food Truck.")
    print ("How can I help you? Please make a selection from the menu: \n")

    menu_items = []
    for category, items in menu.items():
        print(f"{category}:")
        for item_name, item_price in items.items():
            if isinstance(item_price, dict): 
                print(f"  {item_name}:")
                for sub_item, sub_price in item_price.items():
                    print(f"   - {sub_item}: ${sub_price:.2f}")
                    menu_items.append(sub_item)
            else:
                print(f" - {item_name}: ${item_price:.2f}")
                menu_items.append(item_name)
        print()

    return menu_items

# Taking order
def take_order():
    while True:
        menu_selection = input("Enter the section number you want to order from: ")

        if not menu_selection.isdigit() or int(menu_selection) not in range(1, len(menu) +1):
            print("Error: Please enter a valid number.")
            continue

        menu_selection = int(menu_selection)

        item_keys = list(menu.keys())

        selected_category = item_keys[menu_selection - 1]
        items = menu[selected_category]
        item_name = list(items.keys())

        print(f"You selected: {selected_category} -> {item_name}")

        item_name = input(f"Enter the name of the item you would like to order from the {selected_category}: ")

        if isinstance(items.get(item_name), dict):
            print(f"Select a sub-item for {item_name}: {list(items[item_name].keys())}")
            sub_item_name = input(f"Enter the sub-item name you want from {item_name}: ")

            if sub_item_name not in items[item_name]:
                print("Error: Sub-item not found in the selected category.")
                continue 

            item_name = f"{item_name} ({sub_item_name})"
            price = items[item_name.split()[0]][sub_item_name]
        else:
            if item_name not in items: 
                print("Error: Item not in the selected category or menu.")
                continue

            price = items[item_name]

        # Quantity 
        quantity_input = input(f"Enter the quantity for {item_name}: ")

        if not quantity_input.isdigit():
            quantity = 1
        else: 
            quantity = int(quantity_input)

    # Adding order to the order list
        order_list.append({
            "Item name": item_name,
            "Price": price,
            "Quantity": quantity
        })

    # Asking if customer wants to add something to order or thats it 
        while True: 
            continue_ordering = input("Would you like to add anything else? (y/n): ").lower()
            if continue_ordering    == 'y':
                break
            elif continue_ordering == 'n':
                print("Thank you for placing your order. It will be right out.")
                return
            else:
                print("Invalid input. Please enter 'y' to continue or 'n' to finish placing your order.")


# Running the program
menu_items = display_menu()
take_order()

# Printing the receipt
print("Your Order Receipt:")
print(f"{'Item name':<25} | {'Price':<7} | {'Quantity'}")
print("-" * 50)

for order in order_list:
    item_name = order["Item name"]
    price = order["Price"]
    quantity = order["Quantity"]

    print(f"{item_name:<25} | ${price:<6.2f} | {quantity}")


# Calculating the total price of order 

total_price = sum(order['Price'] * order['Quantity'] for order in order_list)

print(f"Total Price: ${total_price:.2f}")

