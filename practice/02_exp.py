age = int(input("Enter your age: "))
day = input("enter your day plan of movie: ")

price = 12 if age >=18 else 8

if day == "wednesday":
    price = price - 2

print(f"Your ticket price is: ${price}")