# from Labs/ python -m API.Lab2.lab2

from ..api import get_json
from pprint import pprint

# # 1. City name -> coordinates
# https://geocoding-api.open-meteo.com/v1/search
#  params: name=Stockholm, count=1
# # 2. Coordinates -> weather
# https://api.open-meteo.com/v1/forecast
#  params: latitude, longitude,
#  current=temperature_2m,wind_speed_10m

# 1 Find the coordinates of a city
# Call the geocoding endpoint with get_json and the params name and count=1. Print
# the whole answer first and look at it before you pick out values. You will see a
# dictionary with a key results, which is a list. The first item in that list is your city, with
# the name, the country, the latitude and the longitude. Then print only the latitude and
# the longitude.
def get_coordinates(city):
    response = get_json(
        "https://geocoding-api.open-meteo.com/v1/search",
        params={"name": city, "count": 1}
    )
    if response and "results" in response:
        latitude = response["results"][0]["latitude"]
        longitude = response["results"][0]["longitude"]
        print(f"{city}, {response["results"][0]["country"]}")
        return latitude, longitude
    return None
    
latitude, longitude = get_coordinates("Stockholm")

# 2 Get the weather for those coordinates
# Call the forecast endpoint with the params latitude, longitude and current set to
# temperature_2m,wind_speed_10m. Print the whole answer first. You will find a key
# current with the values you want, and a key current_units that tells you the units.
def get_forecast(latitude, longitude):
    response = get_json(
        "https://api.open-meteo.com/v1/forecast",
        params={"latitude": latitude, "longitude": longitude,
                "current": "temperature_2m,wind_speed_10m"}
    )
    if response and "current" in response:
        current = response["current"]
        current_units = response["current_units"]
        print(f"Temperature: {current['temperature_2m']} {current_units['temperature_2m']}")
        print(f"Wind speed: {current['wind_speed_10m']} {current_units['wind_speed_10m']}")

# 3 Put it together
# Ask the user for a city with input(). Use the answer from step 1 for the coordinates, and
# then call the forecast. Print one line like this (numbers will differ): Stockholm, Sweden:
# 8.4°C, wind 12.3 km/h. Tip: put each of the two requests in its own function, for
# example find_city(name) and get_weather(lat, lon).
city = input("Input a city: ")
latitude, longitude = get_coordinates(city)
get_forecast(latitude, longitude)

# 4 Handle a city that does not exist
# What happens if the user types a city that does not exist? Handle it so the program
# prints a message and does not crash. Hint: print the answer for a city that does not
# exist, for example asdfghjkl, and look at what is different compared with a city that
# does exist.