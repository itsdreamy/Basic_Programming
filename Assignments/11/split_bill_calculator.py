def split_bill_calculator(total_bill, number_of_people, tip_percentage):
    print(f"Subtotal: Rp. {total_bill}")

    tip = (tip_percentage / 100) * total_bill
    print(f"The tip is {tip_percentage}% (Rp. {tip})")
    
    grandtotal = (total_bill + tip)
    print(f"Grand total is: Rp. {grandtotal}")

    total_split = grandtotal / number_of_people
    print(f"Each person should pay Rp. {total_split}")

total_bill = int(input("Enter the total bill: "))
number_of_people = int(input("How many people are there: "))
tip_percentage = int(input("Enter the tip percentage (e.g.10 for 10%): "))

split_bill_calculator(total_bill, number_of_people, tip_percentage)


# Scenario: You and your friends have finished dinner at a restaurant. You want to create a function called calculate_split_bill to determine how much each person should pay.

# Function Specifications:

# Accepts 3 parameters: total_bill (total food cost), number_of_people (number of diners), and tip_percentage (e.g., 10 for 10%).
# The function must calculate the total bill including the tip, then divide it equally among all participants.
# Required: Return the final amount each person must pay.

# Example Input: calculate_split_bill(300000, 4, 10) (Total bill: Rp300,000, 4 people, 10% tip).