import math
import requests
import math

api_key = 'f0d7d7d323b9aeb4957ffadcd1b9ed65'

city = input('Enter city name: ')
prompt = input('Are you looking for temperature, a description, or both?: ')

url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    temp = data['main']['temp']
    desc = data['weather'][0]['description']

    temp = ((temp - 273.15) * 9/5 + 32)

    if prompt == 'temperature':
        print(f'Temperature: {temp} F')
    elif prompt == 'description':
        print(f'Description: {desc}') 
    else:
        print(f'Temperature: {temp} F')
        print(f'Description: {desc}')   
else:
    print('Error fetching weather data')