import datetime as dt
import random
import smtplib
from zoneinfo import ZoneInfo
import pandas
import os
from dotenv import load_dotenv
load_dotenv()

MY_EMAIL = os.environ["MY_EMAIL"]
PASSWORD = os.environ["MY_EMAIL_APP_PASS"]

now = dt.datetime.now(ZoneInfo("America/Toronto"))
now_day = now.day
now_month = now.month

birthdays = pandas.read_csv("birthdays.csv")
birthdays_dict = {}

for index, row in birthdays.iterrows():
    if (row.month, row.day) not in birthdays_dict:
        birthdays_dict[(row.month, row.day)] = [row]
    else:
        birthdays_dict[(row.month, row.day)].append(row)


if (now_month, now_day) in birthdays_dict:
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(MY_EMAIL, PASSWORD)

        for person in birthdays_dict[(now_month, now_day)]:
            with open(f"./letter_templates/letter_{random.randint(1,3)}.txt", mode="r") as file:
                letter_template = file.read()

            birthday_greeting = letter_template.replace("[NAME]", person["name"])
            server.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=person["email"],
                msg=f"Subject:Happy Birthday!\n\n"
                    f"{birthday_greeting}"
            )