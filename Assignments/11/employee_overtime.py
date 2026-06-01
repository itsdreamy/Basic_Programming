def calculate_overtime_salary(base_salary, total_hours_worked):
    print(f"Your base salary is: Rp. {base_salary}")

    overtime = (total_hours_worked - 40)
    print(f"Your overtime is: {overtime} hour(s)")

    if total_hours_worked > 40:
        ovt_pay = overtime * 50000
    else :
        ovt_pay = 0
    final_salary = base_salary + ovt_pay
    print(f"Your overtime pay is: Rp. {ovt_pay}")
    print(f"Your final salary is: Rp. {final_salary}")

base_salary = int(input("Enter your base salary: "))
total_hours_worked = int(input("How many hours have you worked? (Including overtime): "))
    
calculate_overtime_salary(base_salary, total_hours_worked)



# Scenario: A company pays Rp50,000 per hour for overtime work if an employee works more than 40 hours per week.

# Function Specifications:

# Create a function called calculate_overtime_salary with 2 parameters: base_salary and total_hours_worked.
# If total_hours_worked exceeds 40, calculate the extra hours, multiply them by Rp50,000, and add the result to the base salary.
# If there is no overtime, the employee only receives the base salary.
# Required: Return the employee's final salary.
