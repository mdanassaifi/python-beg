number = int(input("Enter a number: "))

is_prime = True

if number >1:
    for i in range(2,  number):
        if (number & 1) == 0:
            is_prime = False
            break

print(f"{number} is {'a prime' if is_prime else 'not a prime'} number")

