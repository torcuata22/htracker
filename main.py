import requests

USERNAME="marmarq"
TOKEN="1'm7hFr31b4and1d0wha71wan7"

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
    "id":"mygraph1",
    "name":"Health Graph",
    "unit":"minutes",
    "type":"float",
    "color":"ajisai"
}

#need headers for authentication (see docs for key formula, headers is optional kwarg):
headers = {
"X-USER-TOKEN":TOKEN
}
response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
print(response.text)

#to add pixel to graph:

