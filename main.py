import requests
import datetime
import json


def check_rain_forecast() :
    if data[0] > 0.0:
        return 'Będzie padać'
    elif data[0] == 0.0:
        return 'Nie będzie padać'
    else:
        return'Nie wiem'


f = 'history.txt'
latitude = "51.51"
longitude = "-0.13"
tomorrow = datetime.date.today() + datetime.timedelta(days = 1)
formatted_tomorrow = tomorrow.strftime('%Y-%m-%d')
requested_date = input('Podaj we formacie YYYY-mm-dd jaką datę chcesz sprawdzić: ')

if requested_date == '' :
    requested_date = formatted_tomorrow

url = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&"
                   f"hourly=rain&daily=rain_sum&timezone=Europe%2FLondon&start_date={requested_date}&end_date={requested_date}")
data = url.json()['daily']['rain_sum']
print(url.status_code)
print(check_rain_forecast())


print(data)
with open(f, 'w') as file:
    json.dump(data, file)

print(requested_date)