park = int( input("Please enter the parking time in hour (less than 1 hour write 1): "))
pay = 0

for i in range(park) :
    if i > 1 :
        pay += 3000
    else :
        pay += 2500

print(f"Your parking fee is Rp. {pay:,.0f}")