age = int(input("Enter your age: ")) 

if age < 13:
    print("child")
elif age < 20:
    print("teenager")
elif age < 60:
    print("senior")
else:
    print("adult")
