# Vending Machine Program, allowing users to select items and generate a receipt.

def vending_machine():
    # Define available items with their details
    items = {
        1: {"name": "Chips", "price": 1.50, "category": "Snack"},
        2: {"name": "Chocolate Bar", "price": 2.00, "category": "Snack"},
        3: {"name": "Cookies", "price": 1.75, "category": "Snack"},
        4: {"name": "Soda", "price": 1.25, "category": "Drink"},
        5: {"name": "Water", "price": 1.00, "category": "Drink"},
        6: {"name": "Juice", "price": 1.50, "category": "Drink"},
        7: {"name": "Coffee", "price": 2.50, "category": "Drink"},
        8: {"name": "Granola Bar", "price": 1.25, "category": "Snack"}
    }
    
    # Shopping cart to store selected items
    cart = []
    
    print("=" * 50)
    print("          WELCOME TO THE VENDING MACHINE")
    print("=" * 50)
    
    # Display available items
    print("\nAvailable Items:")
    print("-" * 40)
    print(f"{'No.':<4} {'Item':<15} {'Category':<10} {'Price':<8}")
    print("-" * 40)
    
    for item_num, details in items.items():
        print(f"{item_num:<4} {details['name']:<15} {details['category']:<10} ${details['price']:<7.2f}")
    
    print("\nType 'done' when you finish selecting items")
    print("-" * 50)
    
    # Main selection loop
    while True:
        try:
            user_input = input("\nEnter item number to select (or 'done' to finish): ").strip().lower()
            
            if user_input == 'done':
                break
            
            # Convert input to integer
            item_number = int(user_input)
            
            # Check if item exists
            if item_number in items:
                selected_item = items[item_number]
                cart.append({
                    "name": selected_item["name"],
                    "price": selected_item["price"],
                    "category": selected_item["category"]
                })
                print(f"✓ Added {selected_item['name']} - ${selected_item['price']:.2f}")
            else:
                print("❌ Invalid item number. Please try again.")
                
        except ValueError:
            print("❌ Please enter a valid number or 'done' to finish.")
    
    # Generate receipt
    print("\n" + "=" * 50)
    print("                 RECEIPT")
    print("=" * 50)
    
    if not cart:
        print("No items selected. Thank you for visiting!")
        return
    
    # Display selected items
    print(f"{'Item':<20} {'Price':<10}")
    print("-" * 30)
    
    total_cost = 0
    for item in cart:
        print(f"{item['name']:<20} ${item['price']:<9.2f}")
        total_cost += item['price']
    
    print("-" * 30)
    print(f"{'TOTAL':<20} ${total_cost:<9.2f}")
    print("=" * 50)
    print("Thank you for your purchase! 👋")

# Run the vending machine program
if __name__ == "__main__":
    vending_machine()