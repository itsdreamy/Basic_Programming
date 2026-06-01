def convert_minutes(number_of_episodes, duration_per_episodes):
    """This function will calculate how long you have been binge watching in minutes"""
    total_minutes = number_of_episodes * duration_per_episodes
    hours = total_minutes // 60
    minutes = total_minutes % 60
    return hours, minutes

number_of_episodes = int(input("How many episodes have you watched? :"))
duration_per_episodes = int(input("Enter the duration per episodes: "))

hours, minutes = convert_minutes(number_of_episodes, duration_per_episodes)
print(f"You spent {hours} hours and {minutes} minutes")

# Scenario: You often watch TV series and want to know how many hours and minutes you spend watching multiple episodes in one sitting.

# Function Specifications:

# Create a function called convert_minutes with 2 parameters: number_of_episodes and duration_per_episode (in minutes).
# Calculate the total viewing time in minutes, then convert it into hours and remaining minutes.
# Required: The function must return two values at once (using a tuple): hours and remaining minutes.
# Scenario: You often watch TV series and want to know how many hours and minutes you spend watching multiple episodes in one sitting.

# Function Specifications:

# Create a function called convert_minutes with 2 parameters: number_of_episodes and duration_per_episode (in minutes).
# Calculate the total viewing time in minutes, then convert it into hours and remaining minutes.
# Required: The function must return two values at once (using a tuple): hours and remaining minutes.