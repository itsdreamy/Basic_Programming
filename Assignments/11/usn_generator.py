def create_username(full_name, birth_year):
    splitting = full_name.split(" ")
    first_letter = splitting[0]
    birth = birth_year[-2:]
    username = first_letter + birth
    return username


full_name = input("Enter your full name: ").lower()
birth_year = input("Enter yout birth year: ")

print(create_username(full_name, birth_year))

# Scenario: A website wants to automatically generate usernames for new users based on their name and birth year.

# Function Specifications:

# Create a function called create_username with 2 parameters: full_name and birth_year.
# The function should take the first word of full_name (convert it to lowercase), then append the last two digits of birth_year.
# Example: 1998 becomes 98.
# Required: Return the generated username string.

# Hint: You can use the .split() method and string slicing [-2:].