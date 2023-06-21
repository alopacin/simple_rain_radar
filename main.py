import requests
import datetime

tomorrow = datetime.date.today() + datetime.timedelta(days = 1)
ask = input('Podaj we formacie YYYY-mm-dd jaką datę chcesz sprawdzić: ')

if not ask:
    url = requests.get('https://api.open-meteo.com/v1/forecast?latitude=51.51&longitude=-0.13&hourly='
                    'rain&daily=rain_sum&timezone=Europe%2FLondon&start_date={tomorrow}&end_date={tomorrow}')
else:
    url = requests.get('https://api.open-meteo.com/v1/forecast?latitude=51.51&longitude=-0.13&hourly='
                       'rain&daily=rain_sum&timezone=Europe%2FLondon&start_date={ask}&end_date={ask}')
print(tomorrow)
print(ask)