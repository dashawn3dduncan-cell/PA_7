active = True

print("Enter 'quit' to stop adding toppings.")

while active:
    topping = input("What topping would you like on your pizza?")

    if topping.isdigit():
        print("Please enter a valid topping name, not a number.")
        continue

    if topping.lower() == 'quit':
        active = False
    else:
        print(f" I'll add {topping} to your pizza!")