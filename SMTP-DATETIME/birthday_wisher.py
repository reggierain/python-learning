##################### Hard Starting Project ######################

# 1. Update the birthdays.csv with your friends & family's details.
# HINT: Make sure one of the entries matches today's date for testing purposes.

# 2. Check if today matches a birthday in the birthdays.csv
# HINT 1: Only the month and day matter.
# HINT 2: You could create a dictionary from birthdays.csv that looks like this:
# birthdays_dict = {
#     (month, day): data_row
# }
#HINT 3: Then you could compare and see if today's month/day matches one of the keys in birthday_dict like this:
# if (today_month, today_day) in birthdays_dict:

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
# HINT: https://www.w3schools.com/python/ref_string_replace.asp

# 4. Send the letter generated in step 3 to that person's email address.
# HINT: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)

import datetime as dt
import random
import smtplib

import pandas
import os
from dotenv import load_dotenv
load_dotenv()

MY_EMAIL = os.environ["MY_EMAIL"]
PASSWORD = os.environ["MY_EMAIL_APP_PASS"]

now = dt.datetime.now()
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