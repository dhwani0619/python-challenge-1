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
        "Sushi": 17.49,
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
        category_selection = input("Enter the number of the section you want to order form: ")

        if not category_selection.isdigit() or int(category_selection) not in range(1, len(menu) +1):
            print("Error: Please enter a valid section number.")
            continue

        category_keys = list(menu.keys())
        selected_category = category_keys[int(category_selection) - 1]
        items = menu[selected_category]


        print(f"You selected: {selected_category}")
        for idx, (item_name, item_price) in enumerate(items.items(), 1):
            if isinstance(item_price, dict):
                print(f" {idx}. {item_name} (multiple options)")
            else: 
                print (f" {idx}. {item_name} - ${item_price:.2f}")

        item_selection = input(f"Select an item by number: ")

        if not item_selection.isdigit() or int(item_selection) not in range(1, len(items) +1):
            print("Error: Please select a valid item.")
            continue

        item_keys = list(items.keys())
        selected_item = item_keys[int(item_selection) - 1]

        if isinstance(items[selected_item], dict):
            print(f"You selected {selected_item}. Please choose from an option: ")
            sub_items = items[selected_item]
            for idx, (sub_item_name, sub_item_price) in enumerate(sub_items.items(), 1):
                print (f" {idx}. {sub_item_name} - ${sub_item_price:.2f}")

            sub_item_selection = input(f"Select a sub-item by number: ")

            if not sub_item_selection.isdigit() or int(sub_item_selection) not in range(1, len(sub_items) + 1):
                print("Error: Please select a valid sub-item.")
                continue 

            sub_item_keys = list(sub_items.keys())
            selected_sub_item = sub_item_keys[int(sub_item_selection) - 1]
            price = sub_items[selected_sub_item]
            full_item_name = f"{selected_item} ({selected_sub_item})"

        else: 
            full_item_name = selected_item
            price = items[selected_item]

        # Quantity 
        while True: 
            quantity_input = input(f"Enter the quantity for {full_item_name} you would like to order: ")
            if not quantity_input.isdigit():
                print("Invalid input. Setting quantity to 1.")
                quantity = 1
                break 
            else: 
                quantity = int(quantity_input)
                break

    # Adding order to the order list
        order_list.append({
            "Item name": full_item_name,
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

# Printing the receipt
def print_receipt():
    print("Your Order Receipt:")
    print(f"{'Item name':<30} | {'Price':<7} | {'Quantity'}")
    print("-" * 50)

    total_price = 0
    for order in order_list:
        item_name = order["Item name"]
        price = order["Price"]
        quantity = order["Quantity"]
        total_price += price * quantity
        print(f"{item_name:<30} | ${price:<6.2f} | {quantity}")

    print("-" * 50)
    print(f"Total Price: ${total_price:.2f}")

display_menu()
take_order()
print_receipt()