import os
import requests
from twilio.rest import Client
from dotenv import load_dotenv
load_dotenv()

weather_forecast_endpoint = "https://api.openweathermap.org/data/2.5/forecast"

weather_params = {
    "lat": os.getenv("MY_LAT"),
    "lon": os.getenv("MY_LONG"),
    "appid": os.getenv("MY_API"),
    "cnt": 4
}

response = requests.get(weather_forecast_endpoint, params=weather_params)
response.raise_for_status()

weather_hour = response.json()["list"]
for hour in weather_hour:
    weather_id = hour["weather"][0]["id"]
    if int(weather_id) < 531:
        client = Client(os.getenv("TWILIO_SID"), os.getenv("TWILIO_AUTH"))
        message = client.messages.create(
            from_="whatsapp:+14155238886",
            body="It's going to rain today. Remember to bring an umbrella",
            to=f"whatsapp:{os.getenv('MY_WHATSAPP_ID')}"
        )
