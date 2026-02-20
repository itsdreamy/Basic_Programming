num1 = float(input("Input the first number: "))
num2 = float(input("Input the second number: "))

if num1 < num2:
    print("The largest number is: ", num2)
elif num2 < num1:
    print("The largest number is: ", num1)
else :
    print("Numbers are equal")