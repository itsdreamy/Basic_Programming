salary = float( input("Enter your employee's salary: "))
service = int( input("Enter your employee's years of service: "))

bonus = 0

if service >= 10 :
    bonus = (25/100)
elif service >=5 and service <= 9:
    bonus = (15/100)
elif service >= 1 and service <= 4:
    bonus = (5/100)
else :
    bonus = 0

bonus_total = salary * bonus
grand_total = bonus_total + salary

print(f"Thank you for your dedication for the past {service} year(s)")
print(f"Your base salary is Rp. {salary:,.0f}")
print(f"Your bonus is Rp. {bonus_total:,.0f}")
print(f"Your total salary is Rp. {grand_total:,.0f}")