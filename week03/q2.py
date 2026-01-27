print("=" * 50)
print("Question 2: Shopping Cart (Lists - Searching and Removal")
print("-" * 50)
# Concepts: index(), count(), remove(), pop(), in keyword

cart = ["apple", "banana", "milk", "bread", "apple", "eggs"]
apple_cart = cart.count("apple")

# if not found: ValueError: 'milke' is not in list
# apple = cart.remove("apple") # None
milk_location = cart.index("milk")

# just remove "one" apple from the cart
cart.remove("apple")

# remove and print the last item from the cart
removed_item = cart.pop()

print(f"Number of apples: {apple_cart}")
print(f"Position of milk: {milk_location}")
print(f"Remove an apple: {cart}")
print(f"Removed item using pop: {removed_item}")
print("Is banana in cart?", "banana" in cart)
print(f"Final cart: {cart}")

print()
