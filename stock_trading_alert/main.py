
import requests
from twilio.rest import Client
import os
from dotenv import load_dotenv

load_dotenv()

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

# ---------------- STEP 1: STOCK PRICE ---------------- #

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": os.environ["ALPHA_API"]
}

response = requests.get(STOCK_ENDPOINT, params=stock_params)
response.raise_for_status()
stock_data = response.json()["Time Series (Daily)"]

dates = sorted(stock_data.keys(), reverse=True)[:2]

yesterday_price = float(stock_data[dates[0]]["4. close"])
b_yesterday_price = float(stock_data[dates[1]]["4. close"])

difference = (
    (yesterday_price - b_yesterday_price) / b_yesterday_price
) * 100

direction = "🔺" if difference > 0 else "🔻"

if abs(difference) >= 5:

    # ---------------- STEP 2: GET NEWS ---------------- #

    news_params = {
        "apiKey": os.environ["NEWS_API"],
        "q": COMPANY_NAME,
        "sortBy": "publishedAt"
    }

    response = requests.get(NEWS_ENDPOINT, params=news_params)
    response.raise_for_status()
    news_data = response.json()["articles"][:3]

    messages = [
        {
            "title": article["title"],
            "description": article["description"]
        }
        for article in news_data
    ]

    # ---------------- STEP 3: SEND MESSAGES ---------------- #

    client = Client(
        os.environ["TWILIO_SID"],
        os.environ["TWILIO_AUTH"]
    )

    for article in messages:
        message = client.messages.create(
            from_=os.environ["MY_WHATSAPP_ID"],
            to=os.environ["TO_WHATSAPP_ID"],
            body=(
                f"{STOCK}: {direction}{abs(difference):.2f}%\n"
                f"Headline: {article['title']}\n"
                f"Brief: {article['description']}"
            )
        )

        print(message.status)
