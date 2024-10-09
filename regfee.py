member = input("Are you a Member or Non-member of the fitness class? (Yes or No): ")
age = int(input("Kindly input your age: "))

fee = 0

if age < 18:
    if member == "Yes":
        fee = 450
    elif member == "No":
        fee = 650
    else:
        print("Invalid membership information entered.")
elif age >= 18 and age <= 65:
    if member == "Yes":
        fee = 550.00
    elif member == "No":
        fee = 750.00
    else:
        print("Invalid membership information entered.")
elif age >= 65 and age <= 120:
    if member == "Yes":
        fee = 400.00
    elif member == "No":
        fee = 600.00
    else:
        print("Invalid membership information entered.")
else:
    print("Your age entered is invalid. Please try again.")
    
if fee > 0:
    print(f"Your registration fee is: {fee:.2f} pesos. Enjoy your fitness class!")