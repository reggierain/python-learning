import os
import smtplib
import random
import datetime as dt
from dotenv import load_dotenv
load_dotenv()

MY_EMAIL = os.environ["MY_EMAIL"]
MY_EMAIL_APP_PASSWORD = os.environ["MY_EMAIL_APP_PASS"]
TO_EMAIL = os.environ["TO_EMAIL"]

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 6:
    with open("quotes.txt") as file:
        quotes = file.readlines()
        quote = random.choice(quotes)

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as connection:
        connection.login(MY_EMAIL, MY_EMAIL_APP_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=TO_EMAIL,
            msg=f"Subject:Quote of the Day\n\n"
                f"{quote}"
        )
