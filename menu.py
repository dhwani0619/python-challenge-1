# Menu dictionary
menu = {
    "Snacks": {
        "Cookie": .99,
        "Banana": .69,
        "Apple": .49,
        "Granola bar": 1.99
    },
    "Meals": {
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
    "Drinks": {
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
    "Dessert": {
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

# 1. Set up order list. Order list will store a list of dictionaries for
# menu item name, item price, and quantity ordered
order_list = [
    {
        "Item name": "Cookie",
        "Price": .99,
        "Quantity": 1
    },
    {
        "Item name": "Banana",
        "Price": .69,
        "Quantity": 1
    },
    {
        "Item name": "Apple",
        "Price": .49,
        "Quantity": 1
    },
    {
        "Item name": "Granola bar",
        "Price": 1.99,
        "Quantity": 1
    },
    {
        "Item name": "Burrito",
        "Price": 4.49,
        "Quantity": 1
    },
    {
        "Item name": "Teriyaki Chicken",
        "Price": 9.99,
        "Quantity": 1
    },
    {
        "Item name": "Sushi",
        "Price": 7.49,
        "Quantity": 1
    },
    {
        "Item name": "Pad Thai",
        "Price": 6.99,
        "Quantity": 1
    },
    {
        "Item name": "Pizza - Cheese",
        "Price": 8.99,
        "Quantity": 1
    },
    {
        "Item name": "Pizza - Pepproni",
        "Price": 10.99,
        "Quantity": 1
    },
    {
        "Item name": "Pizza - Vegetarian",
        "Price": 9.99,
        "Quantity": 1
    },
    {
        "Item name": "Burger - Chicken",
        "Price": 7.49,
        "Quantity": 1
    },
    {
        "Item name": "Burger - Beef",
        "Price": 8.49,
        "Quantity": 1
    },
    {
        "Item name": "Soda - Small",
        "Price": 1.99,
        "Quantity": 1
    },
    {
        "Item name": "Soda - Medium",
        "Price": 2.49,
        "Quantity": 1
    },
    {
        "Item name": "Soda - Large",
        "Price": 2.99,
        "Quantity": 1
    },
    {
        "Item name": "Tea - Green",
        "Price": 2.49,
        "Quantity": 1
    },
    {
        "Item name": "Tea - Thai iced",
        "Price": 3.99,
        "Quantity": 1
    },
    {
        "Item name": "Tea - Irish breakfast",
        "Price": 2.49,
        "Quantity": 1
    },
    {
        "Item name": "Coffee - Espresso",
        "Price": 2.99,
        "Quantity": 1
    },
    {
        "Item name": "Coffee - Flat white",
        "Price": 2.99,
        "Quantity": 1
    },
    {
        "Item name": "Coffee - Iced",
        "Price": 3.49,
        "Quantity": 1
    },
    {
        "Item name": "Chocolate lava cake",
        "Price": 10.99,
        "Quantity": 1
    },
    {
        "Item name": "Cheescake - New York",
        "Price": 4.99,
        "Quantity": 1
    },
    {
        "Item name": "Cheesecake - Strawberry",
        "Price": 6.49,
        "Quantity": 1
    },
    {
        "Item name": "Australian Pavlova",
        "Price": 9.99,
        "Quantity": 1
    },
    {
        "Item name": "Rice pudding",
        "Price": 4.99,
        "Quantity": 1
    },
    {
        "Item name": "Fried banana",
        "Price": 4.49,
        "Quantity": 1
    },
]
                


# Launch the store and present a greeting to the customer
print("Welcome to the variety food truck.")

# Customers may want to order multiple items, so let's create a continuous
# loop
place_order = True
while place_order:
    print("Please make a selection from the menu: ")
    for category, items in order_list():
        print(f"{category}:")
        for item_name, item_price in items.items():
            if isinstance(item_price, dict): 
                for sub_item_name, dub_item_price in item_price.items():
                    print(f" {item_name} - {sub_item_name}: ${sub_item_price}")
            else:
                print(f" {item_name}: ${item_price}")

menu_selection = input("Enter your selection or 'q' to quit: ").strip()

if not menu_selection.isdigit():
    print("Error: Your input must be a number.")

menu_selection = int(menu_selection)
if menu_selection not in menu_items:
    print ("Error: Your selection is not on the menu.")

item_name = list(menu_items.keys())[menu_selection -1]
quantity = input(f"How many {item_name} would you like? (default is 1) ") or "1"
if not quantity.isdigit():
    quantity = 1
else:
    quantity - int(quantity)

order_list.append({
        "Item name": item_name,
        "Price": menu_items[item_name],
        "Quantity": quantity
})

match input("Would you like to keep ordering? (y/n) ").lower():
    case "y":
        place_order = True
    case "n":
        print("Thank you for your order!")
        place_order = False
    case _: 
        print("Invalid input. Please try again.")

print("nOrder Receipt:")
print("Item name                    | Price | Quantity")
print("-----------------------------|-------|---------")
total_price = 0
for order in order_list:
    item_name = order["Item name"]
    price = order["Price"]
    quantity = order["Quantity"]
    item_price_spaces = " " * (24 - len(item_name))
    price_spaces = " " * (8 - len(str(price)))
    quantity_spaces = " " * (10 - len(str(quantity)))
    print(f"{item_name}{item_price_spaces}| ${price}{price_spaces}| {quantity}{quantity_spaces}")
    total_price += price * quantity

print(f"\nTotal: ${sum(order['Price'] * order['Quantity'] for order in order_list):.2f}")
        

   