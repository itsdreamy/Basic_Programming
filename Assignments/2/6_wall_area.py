import math

length = float( input("Enter the length (m): "))
width = float( input("Enter the width (m): "))
height = float( input("Enter the height (m): "))

coverage_per_can = 10

wall_area = (2 * (length * height)) + (2 * (width * height))

paint_cans = math.ceil(wall_area/coverage_per_can)

print(f"You need {paint_cans} cans of paint to cover total {wall_area} m2 area")
