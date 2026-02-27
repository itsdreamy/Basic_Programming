import math

people = int( input("How many person in the family are? :"))

water_per_person_day = 2.5

water_in_gallon = 19

gallon_price = 19000

total_weekly_cons = people * (water_per_person_day * 7)

gallon_need = math.ceil(total_weekly_cons/water_in_gallon)

total_budget_need = (gallon_need * gallon_price)

print(f"There are {people} people in the house \nTotal weekly consumption is {total_weekly_cons} liter \nYou need to buy {gallon_need} gallons water per week \nTotal budget you need to prepare for a week is Rp. {total_budget_need:,.0f}")

