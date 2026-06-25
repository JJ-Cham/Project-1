# import os

import requests

# API_KEY = os.environ.get("OPENWEATHER_API_KEY")
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
import os
from dotenv import load_dotenv

load_dotenv()

OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")

def get_weather(city, units="metric"):
    if not OPENWEATHER_API_KEY:
        print("Missing OPENWEATHER_API_KEY. Set it as an environment variable.")
        return None

    params = {
        "q": city,
        "units": units,
        "appid": OPENWEATHER_API_KEY,
    }

    try:
        response = requests.get(BASE_URL, params=params, timeout=10)
        response.raise_for_status()
    except requests.exceptions.RequestException as error:
        print(f"Weather request failed: {error}")
        return None

    data = response.json()
    weather_list = data.get("weather", [{}])
    main = weather_list[0] if weather_list else {}

    return {
        "city": data.get("name"),
        "description": main.get("description"),
        "condition": main.get("main"),
        "temp": data.get("main", {}).get("temp"),
        "feels_like": data.get("main", {}).get("feels_like"),
        "humidity": data.get("main", {}).get("humidity"),
        "wind_speed": data.get("wind", {}).get("speed"),
    }
    # return {
    #     "city": data.get("name"),
    #     "description": data["weather"][0]["description"],
    #     "condition": data["weather"][0]["main"],
    #     "temp": data["main"]["temp"],
    #     "feels_like": data["main"]["feels_like"],
    #     "humidity": data["main"]["humidity"],
    #     "wind_speed": data["wind"]["speed"],
    # }


def is_good_weather(weather):
    if weather is None:
        return None

    good_conditions = {"Clear", "Clouds"}
    return weather["condition"] in good_conditions and weather["temp"] >= 10


def suggest_action(city):
    weather = get_weather(city)

    if weather is None:
        return "Could not fetch weather. Try logging a recycling action instead! ♻️"

    if is_good_weather(weather):
        return (
            f"It's {weather['description']} and {weather['temp']}° in "
            f"{weather['city']} — perfect for biking 🚴 or walking 🚶!"
        )

    return (
        f"It's {weather['description']} in {weather['city']} — a great day "
        "for indoor eco actions like recycling ♻️ or saving energy 💡."
    )


if __name__ == "__main__":
    print(get_weather("London"))
    print(suggest_action("London"))
