import requests
import datetime
import json

f = 'history.txt'
latitude = "51.51"
longitude = "-0.13"
tomorrow = datetime.date.today() + datetime.timedelta(days = 1)
formatted_tomorrow = tomorrow.strftime('%Y-%m-%d')
ask = input('Podaj we formacie YYYY-mm-dd jaką datę chcesz sprawdzić: ')

if ask == '':
    url = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&"
                       f"hourly=rain&daily=rain_sum&timezone=Europe%2FLondon&start_date={formatted_tomorrow}&end_date={formatted_tomorrow}")
    data = url.json()['daily']['rain_sum']
    print(url.status_code)
else:
    url = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude{longitude}&"
                       f"hourly=rain&daily=rain_sum&timezone=Europe%2FLondon&start_date={ask}&end_date={ask}")
    data = url.json()['daily']['rain_sum']
    print(url.status_code)

print(data)
with open(f, 'w') as f:
    json.dump(data, f)

print(tomorrow)
print(ask)