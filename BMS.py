menu = {
    'pizza':40,
    'pasta':50,
    'burger':60,
    'salad':70,
    'coffee':80,
}

#Greet
print("Welcome to restorent")
print('pizza:40\nPasta:50\nBurger:60\nsalad:70\ncoffee:80\n')

order_total = 0

item_1 = input("Enter the name of item you want to order: ")

if item_1 in menu:
    order_total += menu[item_1]
    print(f"Your item {item_1} has been added to your order.")
else:
    print(f"ordered item {item_1} is not available yet!")

another_order = input("Do you want to add another item? (yes/no): ")

if another_order.lower() == "yes":
    item_2 = input("Enter the name of secondd order item: ")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"Item {item_2} has been added to order.")
    else:
        print(f"Ordered item {item_2} is not available!")

print(f"The total amount of items is: {order_total}")