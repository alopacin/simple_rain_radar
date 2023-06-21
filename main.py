import requests
import datetime
import json
import os


def check_rain_forecast(data) :
    if data[0] > 0.0:
        return 'Będzie padać'
    elif data[0] == 0.0:
        return 'Nie będzie padać'
    else:
        return 'Nie wiem'


f = "history.txt"
if os.path.exists(f):
    with open(f, 'r') as file:
        try:
            history_of_raining = json.load(file)
        except json.JSONDecodeError:
            history_of_raining = {}

latitude = "51.51"
longitude = "-0.13"
tomorrow = datetime.date.today() + datetime.timedelta(days = 1)
formatted_tomorrow = tomorrow.strftime('%Y-%m-%d')
requested_date = input('Podaj we formacie YYYY-mm-dd jaką datę chcesz sprawdzić: ')

if requested_date == '' :
    requested_date = formatted_tomorrow
if requested_date not in history_of_raining:
    url = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&"
                       f"hourly=rain&daily=rain_sum&timezone=Europe%2FLondon&start_date={requested_date}&end_date={requested_date}")
    data = url.json()['daily']['rain_sum']
    history_of_raining[requested_date] = data
    print(check_rain_forecast(data))
    with open(f, 'a') as file:
        json.dump(history_of_raining, file)
else:
    print("Ta data już została sprawdzona.")


