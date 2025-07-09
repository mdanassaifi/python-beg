order_size = input("Enter the size of your order (small, medium, large): ").lower()
extra_shot = True

if extra_shot:
    coffee = order_size + "  cofee with an extra shot"
else:
    coffee = order_size + "coffee"

print("Your order is:", coffee)