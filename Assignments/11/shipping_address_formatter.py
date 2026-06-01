def format_address (street, city, province, postal_code):
    return f"Street: {street}, City: {city}, {province} ({postal_code})"
    
street = input("Enter street: ")
city = input("Enter city: ")
province = input("Enter province: ")
postal_code = input("Enter postal code: ")
print(f"Address is: {format_address (street, city, province, postal_code)}")


# Scenario: You are building the checkout system for an online shopping application. You need a function that formats a buyer's address into a standard one-line text.

# Function Specifications:

# Create a function called format_address with 4 parameters: street, city, province, and postal_code.
# The function must combine these parameters into the following format:
# Street: [street], City: [city], [province] ([postal_code])
# Required: Return the formatted address string (do not just print it).