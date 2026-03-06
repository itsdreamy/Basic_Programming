distanceTraveled = float(input("Enter the distance traveled (km): "))
travelTime = float(input("Enter the travel time (hours): "))

speed = distanceTraveled / travelTime 

if speed > 80:
    print(f"Your speed is {speed:.2f} km/h \nBe careful, You're on high speed!")
else:
    print(f"Your speed is {speed:.2f} km/h")
