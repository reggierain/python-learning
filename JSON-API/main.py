
import datetime as dt
import os
import smtplib
import time
from zoneinfo import ZoneInfo

import requests
from dotenv import load_dotenv

load_dotenv()

# Configuration
MY_EMAIL = os.environ["MY_EMAIL"]
PASSWORD = os.environ["MY_EMAIL_APP_PASS"]
TO_EMAIL = os.environ["TO_EMAIL"]

MY_LAT = 43.875870
MY_LONG = -79.438271
TIMEZONE = ZoneInfo("America/Toronto")

# Keep track of sunrise, sunset, and alerts
last_sun_date = None
sunrise = None
sunset = None
alert_sent = False

while True:
    try:
        now = dt.datetime.now(TIMEZONE)

        # Update sunrise and sunset once per day
        if last_sun_date != now.date():
            parameters = {
                "lat": MY_LAT,
                "lng": MY_LONG,
                "date": now.date().isoformat(),
                "tz": "America/Toronto"
            }

            response = requests.get(
                "https://api.sunrise-sunset.org/v2",
                params=parameters,
                timeout=15
            )
            response.raise_for_status()
            sun_data = response.json()

            sunrise = dt.datetime.fromisoformat(sun_data["sunrise"])
            sunset = dt.datetime.fromisoformat(sun_data["sunset"])

            last_sun_date = now.date()

        # Get the latest ISS position every 60 seconds
        response = requests.get(
            "http://api.open-notify.org/iss-now.json",
            timeout=15
        )
        response.raise_for_status()

        iss_data = response.json()
        iss_lat = float(iss_data["iss_position"]["latitude"])
        iss_long = float(iss_data["iss_position"]["longitude"])

        # Check whether the ISS is nearby
        iss_nearby = (
            abs(iss_lat - MY_LAT) <= 5
            and abs(iss_long - MY_LONG) <= 5
        )

        # Check whether it's dark
        is_dark = now >= sunset or now < sunrise

        # Send an alert only once per nearby pass
        if iss_nearby and is_dark and not alert_sent:
            with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
                server.login(MY_EMAIL, PASSWORD)
                server.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=TO_EMAIL,
                    msg=(
                        "Subject:ISS Alert!\n\n"
                        "Look up! The ISS is nearby!"
                    )
                )

            alert_sent = True
            print("ISS alert sent!")

        elif not iss_nearby:
            alert_sent = False

        print(f"ISS nearby: {iss_nearby} | Dark: {is_dark}")

    except (requests.RequestException, smtplib.SMTPException,
            OSError, ValueError, KeyError) as error:
        print(f"An error occurred: {error}")

    time.sleep(60)
