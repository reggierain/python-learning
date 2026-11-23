import os
import datetime as dt
from dotenv import load_dotenv
import requests
load_dotenv()

today = dt.datetime.today().strftime('%d/%m/%Y')
time = dt.datetime.today().strftime('%H:%M:%S')

API_ID = os.getenv("APP_ID")
API_KEY = os.getenv("APP_KEY")
SHEETY_AUTH = os.getenv("SHEETY_AUTH")

sheety_ep = "https://api.sheety.co/ba5e45211fad6d1f8d34b427554115e9/workoutTracking/workouts"
api_base_url = "https://app.100daysofpython.dev"
nutrition_ep = f"{api_base_url}/v1/nutrition/natural/exercise"
headers = {
    "x-app-id": API_ID,
    "x-app-key": API_KEY
}

params = {
    "query": input("Tell me which exercises you did: "),
    "weight_kg": 94,
    "height_cm": 165,
    "age": 30,
    "gender": "male"
}

response = requests.post(
    url=nutrition_ep,
    headers=headers,
    json=params
)
result = response.json()

sheety_headers = {
    "Authorization": SHEETY_AUTH
}
workout_params = {
    'workout':
        {
            'date': today,
            'time': time,
            'exercise': result['exercises'][0]['name'],
            'duration': result['exercises'][0]['duration_min'],
            'calories': result['exercises'][0]['nf_calories'],
            'id': result['exercises'][0]['tag_id'],
        }
}

response = requests.post(url="https://api.sheety.co/ba5e45211fad6d1f8d34b427554115e9/workoutTracking/workouts", headers=sheety_headers, json=workout_params)
print(response.text)