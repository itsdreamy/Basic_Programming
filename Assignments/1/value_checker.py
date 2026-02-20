number = float(input("Input a number: "))

if number > 0:
    print(number, "is positive number")
elif number < 0:
    print(number, "is negative number")
elif number == 0: 
    print(number, "is zero")
else: 
    print("Invalid Number")