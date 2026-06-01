def calculate_discount(total) :
    if total <= 100000 :
        discount = 0
    elif total > 100000 :
        discount = 0.25 * total
    final_price = total - discount
    return discount, final_price

discount, final_price = calculate_discount(250000)
print(f'Your total is Rp. {final_price}')
print(f'You got {discount}')