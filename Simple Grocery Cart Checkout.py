# Predefined dictionary of groceries with prices
groceries = {
    "apple": 0.50,
    "banana": 0.25,
    "bread": 2.50,
    "milk": 3.00,
    "eggs": 4.00,
    "cheese": 5.00,
    "chicken": 8.00,
    "rice": 1.50,
    "pasta": 1.25,
    "tomato": 0.75,
    "potato": 0.40,
    "onion": 0.60
}

def display_available_groceries():
    """Display available groceries with prices"""
    print("\n" + "="*40)
    print("AVAILABLE GROCERIES")
    print("="*40)
    for item, price in groceries.items():
        print(f"{item.capitalize():<15} - ${price:.2f}")
    print("="*40)

def get_quantity():
    """Get and validate quantity input from user"""
    while True:
        try:
            quantity = int(input("Enter quantity: "))
            if quantity <= 0:
                print("Please enter a positive number.")
                continue
            return quantity
        except ValueError:
            print("Invalid input! Please enter a valid number.")

def calculate_bill(cart):
    """Calculate and display the final bill"""
    print("\n" + "="*50)
    print("FINAL BILL")
    print("="*50)
    
    total_amount = 0
    
    # Display each item with details
    for item, quantity in cart.items():
        if item in groceries:
            price = groceries[item]
            subtotal = price * quantity
            total_amount += subtotal
            print(f"{item.capitalize():<15} {quantity:>3} x ${price:>5.2f} = ${subtotal:>6.2f}")
    
    print("="*50)
    print(f"{'TOTAL AMOUNT:':<15} ${total_amount:>6.2f}")
    print("="*50)

def main():
    """Main function to run the grocery cart checkout system"""
    cart = {}
    
    print("Welcome to the Simple Grocery Store!")
    print("Type 'checkout' when you're done shopping.")
    print("Type 'list' to see available items.")
    
    while True:
        display_available_groceries()
        
        # Get item from user
        item = input("\nEnter item name (or 'checkout' to finish): ").lower().strip()
        
        # Check if user wants to checkout
        if item == "checkout":
            if not cart:
                print("Your cart is empty. Thank you for visiting!")
            else:
                calculate_bill(cart)
            break
        
        # Display available items if requested
        if item == "list":
            continue
        
        # Check if item exists in our grocery list
        if item not in groceries:
            print(f"Sorry, '{item}' is not available. Please choose from the list above.")
            continue
        
        # Get quantity for valid item
        print(f"You selected: {item.capitalize()} - ${groceries[item]:.2f}")
        quantity = get_quantity()
        
        # Add to cart or update quantity
        if item in cart:
            cart[item] += quantity
            print(f"Updated {item.capitalize()} quantity to {cart[item]}")
        else:
            cart[item] = quantity
            print(f"Added {quantity} {item.capitalize()}(s) to your cart")
        
        # Show current cart summary
        print(f"\nCurrent cart: {len(cart)} item(s)")
        for cart_item, qty in cart.items():
            print(f"  - {cart_item.capitalize()}: {qty}")

# Run the program
if __name__ == "__main__":
    main()