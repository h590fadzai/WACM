from urllib.request import urlopen
import json
import datetime

# Init Variables
welcomeMessage = "--- Weather Pyvien ---"
date = datetime.datetime.now()
date = date.strftime("%Y/%-m/%-d")

# Welcome to the Weather API
print(welcomeMessage)

# User search
userSearch = input("Where would you like to check the weather?\n> ")

# Get WOEID
link = 'https://www.metaweather.com/api/location/search/?query=' + userSearch
response = urlopen(link)
data = json.loads(response.read())
woeid = data[0]['woeid']

# Get Weather
link = 'https://www.metaweather.com/api/location/' + str(woeid) + '/' + date
response = urlopen(link)
data = json.loads(response.read())

# Print it to the screen
print("Type of weather: " + data[0]["weather_state_name"])
print("Minimum Temperature: " + str(round(data[0]["min_temp"])))
print("Maximum Temperature: " + str(round(data[0]["max_temp"])))
