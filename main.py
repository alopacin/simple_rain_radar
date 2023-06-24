# import modulow
import requests
import datetime
import json
import os

# funkcja wyswietlajaca czy bedzie padac w sprawdzanym dniu
def check_rain_forecast(data) :
    if data[0] > 0.0:
        return 'Będzie padać'
    elif data[0] == 0.0:
        return 'Nie będzie padać'
    else:
        return 'Nie wiem'


# czesc odpowiadajaca za obsluge bledu dotyczacego tego czy dany plik istnieje
f = "history.txt"
if os.path.exists(f):
    with open(f, 'r') as file:
        try:
            history_of_raining = json.load(file)
        except json.JSONDecodeError:
            history_of_raining = {}

# nadanie zmiennych. domyslnie ustawiona szerokosc i dlugosc geograficzna na Londyn
latitude = "51.51"
longitude = "-0.13"

# przypisanie do zmiennej tomorrow dnia jutrzejszego
tomorrow = datetime.date.today() + datetime.timedelta(days = 1)
formatted_tomorrow = tomorrow.strftime('%Y-%m-%d')

# zapytanie do uzytkownika
requested_date = input('Podaj we formacie YYYY-mm-dd jaką datę chcesz sprawdzić: ')

# jezeli uzytkownik nic nie wpisal zostana wyswietlone opady na dzien jutrzejszy
if requested_date == '' :
    requested_date = formatted_tomorrow

# jezeli wczesniej nie bylo wprowadzonej daty to zostanie wyslane zapytanie do api i zostanie obsluzony blad
# jezeli uzytkownik zle wpisze date (zostanie wyswietlony komunikat i program zakonczy dzialanie)
if requested_date not in history_of_raining:
    try:
        datetime.datetime.strptime(requested_date, '%Y-%m-%d')
    except ValueError:
        print('Nieprawidłowy format daty. Wprowadź datę we formacie YYYY-mm-dd lub zostaw puste'
              ' aby sprawdzić jutrzejszy dzień')
        exit()
    url = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&"
                       f"hourly=rain&daily=rain_sum&timezone=Europe%2FLondon&start_date={requested_date}"
                       f"&end_date={requested_date}")
    data = url.json()['daily']['rain_sum']
    history_of_raining[requested_date] = data
    print(check_rain_forecast(data))

# zapisanie danych do pliku we formacie json
    with open(f, 'w') as file:
        json.dump(history_of_raining, file)

# jezeli data byla juz sprawdzana zapytanie do api zostanie pominiete i
# wyswietlone zostana dane ze wczesniejszej historii
else:
    data = history_of_raining[requested_date]
    print(check_rain_forecast(data))
    print("Ta data już została sprawdzona.")


