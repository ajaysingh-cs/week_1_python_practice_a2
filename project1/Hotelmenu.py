menu = {
    'pizza': 60,
    'pasta': 50,
    'burger': 60,
    'salad': 70,
    'coffee': 80
}

print("Welcome to AJBuilds Restaurant")

while True:

    print("\npizza : rs 60\npasta : rs 50\nburger : rs 60\nsalad : rs 70\ncoffee : rs 80")

    order_total = 0

    item_1 = input("\nEnter the name of item you want to order = ").lower()

    if item_1 == "exit" or item_1 == "quit":
        print("Thank you for visiting AJBuilds Restaurant")
        break

    if item_1 in menu:
        order_total += menu[item_1]
        print(f"your item {item_1} has been added to your order")

    else:
        print(f"Ordered item {item_1} is not available yet!")

    another_order = input("Do you want to add another item ? (yes/no) = ").lower()

    while another_order == "yes":

        item_2 = input("Enter second item = ").lower()

        if item_2 in menu:
            order_total += menu[item_2]
            print(f"item {item_2} has been added to order")

        else:
            print(f"Ordered item {item_2} is not available!")

        another_order = input("Do you want to add another item ? (yes/no) = ").lower()

    print(f"\nThe total amount to pay is rs {order_total}")