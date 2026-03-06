totalPurchase = int( input("Enter your total purchase amount: "))

if totalPurchase >= 500000 :
    discount = (20/100)
    subtotal = discount * totalPurchase
elif totalPurchase >= 250000 : 
    discount = (10/100)
    subtotal = discount * totalPurchase
else :
    discount = 0
    subtotal = discount * totalPurchase

grandTotal = totalPurchase - subtotal
print(f"Your total purchase amount is Rp. {totalPurchase:,.0f}")
print(f"Your discount is {discount} (Rp. {subtotal:,.0f})")
print(f"Your total is Rp. {grandTotal:,.0f}")

