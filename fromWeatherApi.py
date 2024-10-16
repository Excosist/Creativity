import requests
import sys

api_key = '381215fd24974c01a8d130248240605'

user_input = input('Enter city: ')

weather_data = requests.get(
    f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={user_input}")



last_updated = weather_data.json()["current"]["last_updated"]
temp_c = weather_data.json()["current"]["temp_c"]
weather = weather_data.json()["current"]["condition"]["text"]
humidity = weather_data.json()["current"]["humidity"]
temp_cfl = weather_data.json()["current"]["feelslike_c"]

print(f"The weather in {user_input} is {weather}")
print(f"The temperature today is {temp_c}°C but feels like {temp_cfl} and the humidity level is {humidity}")
print(f"Data was last updated on {last_updated}")

sys.exit("Thank you for using")