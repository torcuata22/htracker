import requests
from datetime import datetime #use this module to automate date

USERNAME="marmarq"
TOKEN="1'm7hFr31b4and1d0wha71wan7"
GRAPH_ID= "mygraph1"

#As per pixela documentation:
pixela_endpoint = 'https://pixe.la/v1/users'
user_params = {
    "token": TOKEN,
    "username":USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

  #commented this out after user was successfully created  
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

#create graph:

graph_endpoint= f"{pixela_endpoint}/{USERNAME}/graphs"

#make post request:

graph_config={
    "id":GRAPH_ID,
    "name":"Health Graph",
    "unit":"minutes",
    "type":"float",
    "color":"ajisai"
}

#need headers for authentication (see docs for key formula, headers is optional kwarg):
headers = {
"X-USER-TOKEN":TOKEN
}
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

#to add pixel to graph: /v1/users/<username>/graphs/<graphID>
pixel_creation_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}'
today = datetime.now()
#print(today.strftime("%Y%m%d"))
pixel_data={
"date":today.strftime("%Y%m%d"),
"quantity":"30"
}

response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
print(response.text)

#PUT and DELETE, from docs:
#PUT: url=/v1/users/<username>/graphs/<graphID>/<yyyyMMdd>
#need headers
#need update_config: quantity as string (required)
