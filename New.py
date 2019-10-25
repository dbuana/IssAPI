# basic python API
import requests

response = requests.get("http://api.open-notify.org/this-api-doesnt-exist")
print(response)

#200: Everything went okay, and the result has been returned (if any).
#301: The server is redirecting you to a different endpoint. This can happen when a company switches domain names, or an endpoint name is changed.
#400: The server thinks you made a bad request. This can happen when you don’t send along the right data, among other things.
#401: The server thinks you’re not authenticated. Many APIs require login ccredentials, so this happens when you don’t send the right credentials to access an API.
#403: The resource you’re trying to access is forbidden: you don’t have the right permissions to see it.
#404: The resource you tried to access wasn’t found on the server.
#503: The server is not ready to handle the request.

# Here we will be collecting data from the famous international space station
members = requests.get("http://api.open-notify.org/astros.json")
members_json = members.json()
#print(members_json)
print("Number of people currently in International Space Station: ", members_json["number"])

for x in members_json["people"]:
    print(x["name"])

    
                                   

    

    



