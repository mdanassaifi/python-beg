# simple calculator

print("Welcome to the calculator")
print("Please enter your choice")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
choice = int(input("Enter your choice: "))

if choice == 1:
    print("Enter two numbers")
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    print(num1 + num2)
elif choice == 2:
    print("Enter two numbers")
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    print(num1 - num2)
elif choice == 3:
    print("Enter two numbers")
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    print(num1 * num2)
elif choice == 4:
    print("Enter two numbers")
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    print(num1 / num2)
else:
    print("Invalid choice, please try again")