distance = int(input("Enter the distance: "))

if distance < 3:
    transport = "Walk"
elif distance < 15:
    transport = "Bike"
else :
    transport = "Car"

print("Ai recommend you to use:", transport)