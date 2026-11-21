import requests
import datetime as dt
import os
from dotenv import load_dotenv
load_dotenv()

# create account
pixela_endpoint = "https://pixe.la/v1/users"
# pixela_user_params = {
#     "token": os.getenv("PIXELA_TOKEN"),
#     "username": os.getenv("PIXELA_USERNAME"),
#     "agreeTermsOfService": "yes",
#     "notMinor": "yes"
# }

# create account
# response = requests.post(url=pixela_endpoint, json=pixela_user_params)
# print(response.text)

# # create graph
pixela_graph_ep = f"{pixela_endpoint}/{os.getenv('PIXELA_USERNAME')}/graphs"
pixela_graph_params = {
    "id": "graph1",
    "name": "Daily Coding Hours",
    "unit": "hours",
    "type": "float",
    "color": "kuro"
}

headers = {
    "X-USER-TOKEN": os.getenv("PIXELA_TOKEN")
}

# response = requests.post(url=pixela_graph_ep, json=pixela_graph_params, headers=headers)
# print(response.text)

today = dt.datetime.now().strftime("%Y%m%d")

post_pixela_endpoint = f"{pixela_graph_ep}/{pixela_graph_params['id']}"

post_pixela_params = {
    "date": today,
    "quantity": "1.5"
}

response = requests.post(url=post_pixela_endpoint, json=post_pixela_params, headers=headers)
print(response.text)