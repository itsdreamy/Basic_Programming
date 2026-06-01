cars = ["Ford", "Toyota", "Suzuki", "Avanza", "Pajero", "Kijang"]
cars.append("BMW")
#cars = ["Ford", "Toyota", "Suzuki", "Avanza", "Pajero", "Kijang", "BMW"]
cars.pop(0)
#cars = ["Toyota", "Suzuki", "Avanza", "Pajero", "Kijang", "BMW"]
cars[0] = "Kijang"
#cars = ["Kijang" "Suzuki", "Avanza", "Pajero", "Kijang", "BMW"]
cars.remove("Kijang")
#cars = ["Suzuki", "Avanza", "Pajero", "BMW"]
print(cars[0])
cars.insert(1, "Lambo")
print(cars)

x = len(cars)

for i, car in enumerate(cars):
    print(i, car)