def calculate_loyalty_points(total_transaction, member_status):
    if member_status == False:
        return 0
    else:
        point = total_transaction // 20000
        return point
    
total_transaction = int(input("Enter the total transaction: "))
member_status = input("Are you a member? (Yes/No): ").lower()
if member_status == 'yes':
    member_status = True
else:
    member_status = False

point = calculate_loyalty_points(total_transaction, member_status)
print(f"Your total is Rp. {total_transaction}")
print(f"You just earned {point} loyalty points")


# Scenario: A grocery store rewards loyal customers with shopping points.

# Function Specifications:

# Create a function called calculate_loyalty_points with 2 parameters: total_transaction and member_status (Boolean: True/False).
# If member_status is False, immediately return 0 without performing any calculations.
# If member_status is True, the customer earns 1 point for every Rp20,000 spent.
# Use floor division (//) to calculate the number of points.
# Required: Return the total points earned.