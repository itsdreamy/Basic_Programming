initial_price = int( input("Enter your initial laptop price: "))
usage_time = float( input("Enter how long since you buy your laptop (year): "))

salvage_value = 2000000
economic_life = 4

annual_depriciation = (initial_price - salvage_value) / economic_life

laptop_value = initial_price - (usage_time * annual_depriciation)

print(f"Annual depriciation is Rp. {annual_depriciation:,.0f}")
print(f"Laptop value after {usage_time} year(s) is Rp. {laptop_value:,.0f}")