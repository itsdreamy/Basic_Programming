total_hour = int( input("Enter your total hour(if there's minutes, add it to the next input): "))
minutes_left = int( input("Enter your total hour in minute: "))

hourly_rate = 85000

decimal_hours = total_hour + (minutes_left/60)

total_payment = hourly_rate * decimal_hours

print(f"The hourly rate is: {hourly_rate:,.0f}\nYour total payment is: {total_payment:,.0f}")