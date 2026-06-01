def calculate_age(birth_year):
    """This Function calculating your age by your birthyear"""
    age = 2026 - birth_year
    return age

def greetings(name, phone, address = None):
    print(f"Hello, {name}!")
    if address != None :
        print(f"Your address is, {address}!")
    else :
        print()
    print(f"Your phone number is {phone}")

def group_by_age(age):
    if age < 2 and age > 0:
        return "Babies"
    elif age <= 5:
        return "Toddlers"
    elif age <= 10:
        return "Kids"
    elif age <= 17:
        return "Teenagers"
    elif age >= 18:
        return "Adult"
    else :
        return "Invalid Input!"
    
name = input("Enter your name: ")
phone = input("Enter your phone number: ")
birth_year = int(input("Enter your birth year: "))
address = input("Enter your address (Optional): ")

greetings(name, phone, address)
print(f"Your age is {calculate_age(birth_year)}")
print(f"You are an {group_by_age(calculate_age(birth_year))}")