import requests
import os
from dotenv import load_dotenv

def get_weather():
    load_dotenv()
    api_key = os.getenv("api_key")
    city = input("Enter the city: ")
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        weather = data["weather"][0]["main"]
        description = data["weather"][0]["description"]
        temp = data["main"]["temp"] - 273.15
        feels_like = data["main"]["feels_like"] - 273.15
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]
        city_name = data["name"]

        print(f"Weather in {city_name}:")
        print(f"Condition: {weather} - {description}")
        print(f"Temperature: {temp:.2f}°C")
        print(f"Feels Like: {feels_like:.2f}°C")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_speed} m/s")
    else:
        print("Could not retrieve data. Check the city name or API key.")
