# ==============================
# 🛒 SHOPPING BILLING SYSTEM
# ==============================

# items will store the names of purchased items
items = []

# total will store the total bill amount
total = 0

# Infinite loop to allow continuous item input until user exits
while True:
    # Ask user to input item name or 'q' to quit
    item = input("Enter the name of the item (press q to exit): ")

    # If the user enters 'q' or 'Q', exit the loop
    if item.lower() == 'q':
        print("\n========================")
        print(f"🧾 Total bill: ₹{total}")
        print("🙏 Thank you! Visit again.")
        print("========================")
        break  # terminates the loop

    # If user entered an actual item name
    else:
        # Add item to the items list
        items.append(item)

        # Ask for cost and quantity, cast to int since input() returns string
        cost = int(input(f"Enter the cost of '{item}': ₹"))
        quantity = int(input(f"Enter how many '{item}' you want to buy: "))

        # Multiply cost and quantity to get subtotal and add to total
        total += cost * quantity

        print(f"🧾 Subtotal for {item} x {quantity} = ₹{cost * quantity}")
        print("---------------------------------")
