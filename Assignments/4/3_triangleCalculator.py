side1 = float(input("Input the length of the first side: "))
side2 = float(input("Input the length of the first side: "))
side3 = float(input("Input the length of the first side: "))

if side1 == side2 == side3:
    print("Triangle Type: Equilateral triangle")
elif side1 == side2 or side2 == side3 or side1 == side3:
    print("Triangle Type: Isosceles triangle")
else:
    print("Triangle Type: Scalene triangle")