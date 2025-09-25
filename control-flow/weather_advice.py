# This script provides clothing recommendations based on user input for weather conditions.
# Prompt the user for the current weather.
weather = input("What's the weather like today? (sunny/rainy/cold): ").lower()
# Use conditional statements to provide advice based on the weather.
if weather == "sunny":
    print("Wear a t-shirt and sunglasses.")
elif weather == "rainy":
    print("Don't forget your umbrella and a raincoat.")
elif weather == "cold":
    print("Make sure to wear a warm coat and a scarf.")
else:
    print("Sorry, I don't have recommendations for this weather.")