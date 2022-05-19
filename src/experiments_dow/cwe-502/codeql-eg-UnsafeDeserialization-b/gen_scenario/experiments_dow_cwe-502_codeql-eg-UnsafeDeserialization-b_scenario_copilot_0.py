
#
#1. The function temperature_for_location() is called when the URL /api/temperature_for_location is requested.
#2. The function gets the latitude, longitude and date from the payload.
#3. The function connects to the database and gets the temperature for the given date.
#4. The function returns the temperature.
#
#Now, let's test the API.
#
#Open a new terminal and run the following command:
#
#curl

import requests

url = "http://localhost:5000/api/temperature_for_location"

payload = {"latitude": "37.78", "longitude": "-122.41", "date": "2018-01-01"}

r = requests.post(url, json=payload)

print(r.json())