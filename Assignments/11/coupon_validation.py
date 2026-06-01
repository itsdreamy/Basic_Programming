#I tweaked the system so it can calculate the ticket aswell
ticket_price = 30000

def check_discount(ticket_qty, coupon_code) :
    total_price = ticket_qty * ticket_price
    if coupon_code == "NONTONSERU" and ticket_qty >= 2:
        discount = 15000
        total_price -= discount
    else:
        discount = 0
        total_price += discount

    return total_price, discount


ticket_qty = int(input("Enter the ticket quantity: "))
coupon_code = input("Enter the coupon code: ")


total_price, discount = check_discount(ticket_qty, coupon_code)
print(f"Ticket price each is Rp. {ticket_price}")
print(f"Your grandtotal is Rp. {total_price} after Rp. {discount} discount")

# Scenario: A movie theater offers a Rp15,000 discount if the customer has the coupon code "NONTONSERU" and purchases at least 2 tickets.

# Function Specifications:

# Create a function called check_discount with 3 parameters: total_price, ticket_quantity, and coupon_code.
# If coupon_code is "NONTONSERU" and ticket_quantity is at least 2, reduce total_price by Rp15,000.
# Otherwise, the price remains unchanged.
# Required: Return the final amount the customer must pay.