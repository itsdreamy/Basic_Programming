print("Welcome to rectangle area! The input will need meters measurement, please open our distance conversion if you need help for the conversion!")
length = float(input("Please enter the length in meter: "))
width = float(input("Please enter the width in meter: "))

area = length * width
perimeter = 2 * (length + width)

print(f"The area of the rectangle is {area} m")
print(f"The perimeter of the rectangle is {perimeter} m")

if area > 100:
    print(f"{area} m is a large area!")