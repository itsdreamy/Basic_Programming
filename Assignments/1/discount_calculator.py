price = float(input("Enter the item price: "))

if(price >= 100000):
    discount = 0.1
else:
    discount = 0

total_discount = price * discount
grand_total = price - total_discount

print(f"Item Price : {price:,.0f}")
print(f"Total discount : {total_discount:,.0f}")
print(f"Your grand total is : {grand_total:,.0f}")