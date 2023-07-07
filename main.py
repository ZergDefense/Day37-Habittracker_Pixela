import datetime
import os

import requests

TOKEN = os.environ['PIXELA_TOKEN']
USERNAME = os.environ['PIXELA_USER']
GRAPH_ID = os.environ['PIXELA_GRAPH']

# create a user:

pixela_user_endpoint = "https://pixe.la/v1/users"
#
# parameters = {
#     "token": TOKEN,
#     "username": USERNAME,
#     "agreeTermsOfService": "yes",
#     "notMinor": "yes",
# }
#
# response = requests.post(url=pixela_user_endpoint, json=parameters)
# print(response.text)


# create a graph:

pixela_graph_endpoint = f"{pixela_user_endpoint}/{USERNAME}/graphs"
#
# graph_config = {
#     "id": "GRAPH_ID",
#     "name": "Training Graph",
#     "unit": "pc",
#     "type": "int",
#     "color": "momiji",
# }
#
# headers = {
#     "X-USER-TOKEN": TOKEN
# }
#
# response = requests.post(pixela_graph_endpoint, json=graph_config, headers=headers)
# print(response.text)


# Post value to the graph:

pixela_value_endpoint = f"{pixela_graph_endpoint}/{GRAPH_ID}"
today = datetime.datetime(year=2023, month=7, day=7)
#
headers = {
    "X-USER-TOKEN": TOKEN
}
#
request_body = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "10",
}
#
# response = requests.post(url=pixela_value_endpoint, json=request_body, headers=headers)
# print(response.text)


# Modify value in the graph:

pixela_value_update_endpoint = f"{pixela_graph_endpoint}/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

response = requests.put(url=pixela_value_update_endpoint, json=request_body, headers=headers)
print(response.text)


# Delete value in the graph:

# response = requests.delete(url=pixela_value_update_endpoint, headers=headers)
# print(response.text)
