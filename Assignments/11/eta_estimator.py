def estimate_arrival(distance_km, weather_con):
    travel_time = distance_km * 3
    if weather_con == "rainy":
        travel_time += 10
    else:
        travel_time += 0
    return travel_time

distance_km = int(input("Enter distance in km: "))
weather_con = input("Enter weather condition (rainy/sunny): ").lower()

print(f"Estimated arrival is in {estimate_arrival(distance_km, weather_con)} minutes")


# Scenario: A ride-hailing application needs a system to estimate arrival time based on distance and weather conditions.

# Function Specifications:

# Create a function called estimate_arrival with 2 parameters: distance_km and weather_condition.
# By default, each kilometer takes 3 minutes of travel time.
# However, if weather_condition is "rainy", add 10 extra minutes to the total travel time (because the driver travels more slowly).
# Required: Return the total estimated travel time in minutes.