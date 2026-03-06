print("Welcome to Distance Converter!")
kilometers = float(input("Please enter the distance in kilometers(km): "))

meter = kilometers * 1000
cm = meter * 100
miles = kilometers * 0.621371 

print(f"{kilometers:,.0f} km is {meter:,.0f} m")
print(f"{kilometers:,.0f} km is {cm:,.0f} cm")
print(f"{kilometers:,.0f} km is {miles:,.0f} miles")