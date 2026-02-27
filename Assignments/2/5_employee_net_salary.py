base_salary = int( input("Enter your base salary: "))
allowance = int( input("Enter your allowance: "))


bpjs = 0.02
tax = 0.05

gross_salary = base_salary + allowance
deduction = gross_salary * (bpjs + tax)

salary = gross_salary - deduction

print(f"Your salary is Rp. {salary:,.0f}")