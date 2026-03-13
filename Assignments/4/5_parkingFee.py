vehicle_type = input("Enter your vehicle type (motorcycle/car/bus): ")
parking_duration = float( input("Enter your parking duration (hour): "))

lower = vehicle_type.lower()
fee = 0
addition_hour = 0

if parking_duration <= 1:
    if lower == "motorcycle":
        fee = 1
    elif lower == "car":
        fee = 2
    elif lower == "bus":
        fee = 3
    else:
        addition_hour = 0

elif parking_duration > 1:
    if lower == "motorcycle":
        addition_hour = 0.5
    elif lower == "car":
        addition_hour = 1
    elif lower == "bus":
        addition_hour = 2
    else:
        addition_hour = 0

parking_fee = fee + (addition_hour * parking_duration)

print(f"Your parking fee is {parking_fee} USD")