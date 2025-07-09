number = int(input("Enter a number: "))
original_number = number
factorial = 1

while number > 0:
    factorial *= number
    number -= 1

print(f"Factorial {original_number} is {factorial}")