import requests

#response = requests.get("http://api.open-notify.org/this-api-doesnt-exist")
#print(response.status_code) should return 404 error code

response = requests.get("http://api.open-notify.org/astros")
print(response.status_code)
#This should return 200 if successful
