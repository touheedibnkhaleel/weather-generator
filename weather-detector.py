
import requests

apikey = "cb771e45ac79a4e8e2205c0ce66ff633"
city = input("Enter city: ")

url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={apikey}"

response = requests.get(url).json()

print(response)
