score = int(input("Enter your score: "))
 
if score >=101:
    print("please enter a valid score")
    exit()

if score >= 90:
    print("You got an A!")
elif score >= 80:
    print("You got a B!")
elif score >= 70:
    print("You got a C!")
else:
    print("You got a F!")