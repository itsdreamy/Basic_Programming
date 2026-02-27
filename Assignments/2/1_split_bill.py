total_person = int( input("How many person are there? :"))
bill = int( input("How much is the total? :"))

tax = 0.1 * bill
grand_total = bill + tax

split_bill = grand_total / total_person

print(f"Subtotal: {bill:,.0f}")
print(f"Tax(10%): {tax}")
print(f"Grand Total: {grand_total:,.0f}")
print(f"There are {total_person} people, so each person should pay: {split_bill:,.0f}")