usage = float( input("Enter your electricity usage (kWh): "))
price = 0

if usage <= 100 :
    price = 0.10
elif usage <= 300 :
    price = 0.15
elif usage > 300 :
    price = 0.20

totalPrice = price * usage

print(f"Your electricity usage is: {usage} kWh")
print(f"Your electricity usage is: {totalPrice} USD")
