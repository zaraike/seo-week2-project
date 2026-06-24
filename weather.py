"""Weather and AI tip functions for the Weather Watchlist app."""

import os

import requests
from dotenv import load_dotenv
from google import genai

load_dotenv()

WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
WEATHER_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    """Return current weather for a city as a dicitonary
    
    Returns None if the city is not found or the request fails.
    """
    params = {
        "q": city,
        "appid": WEATHER_API_KEY,
        "units": "imperial",
    }
    try: 
        response = requests.get(WEATHER_URL, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
        return{
            "temp": round(data["main"]["temp"]),
            "humidity": data["main"]["humidity"],
            "condition": data["weather"][0]["main"],
        }
    except requests.RequestException:
        return None
    except (KeyError, IndexError):
        return None
    
def get_tip(weather):
    """Return a one-line clothing tip based on weather dictionary.

    Falls back to a simple message if the AI call fails.
    """
    prompt = (
        f"Weather is {weather['temp']}F, {weather['condition']}, "
        f"{weather['humidity']}% humidity. Give a one-line tip on "
        f"what to wear or bring. Keep it under 15 words."
    )
    try:
        client = genai.Client(api_key=GEMINI_API_KEY)
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
        )
        return response.text.strip()
    except Exception:
        return "Weather loaded, tip unavilable right now."
