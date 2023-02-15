import requests

#As per pixe.la documentation:
pixela_endpoint = 'https://pixe.la/v1/users'
user_params = {
    "token": "1'm7hFr31b4and1d0wha71wan7",
    "username":"Lokito",
    "agreeTermsOfService": "yes",
    "notMinor": "no",
}
    
response = requests.post(url=pixela_endpoint, json=user_params)