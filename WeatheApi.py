import requests

api_key = "" # input your api key details
#base_url ="http://api.openweathermap.org/data/2.5/weather"
base_url ="http://api.openweathermap.org/geo/1.0/direct"
city = input("Enter a city: ")
state = input("Enter a state: ")
country = "USA"

#request_url = f"{base_url}?appid ={api_key}&q={city}"
request_url = f"{base_url}?q={city}&limit={2}&appid={api_key}"
print(request_url)
response = requests.get(request_url)
if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print("An Error Occured! " , response.status_code)
    