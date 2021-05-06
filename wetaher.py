import datetime
from config import open_weather_token
from pprint import pprint

import requests
import os
import sys
sys.path.append(os.path.dirname(__file__))


def get_weather(city, open_weather_token):
    try:
        request = requests.get(
            f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={open_weather_token}&units=metric')
        data = request.json()
        pprint(data)

        city = data['name']
        weather = data['main']['temp']
        humidity = data['main']['humidity']
        pressure = data['main']['pressure']
        wind_speed = data['wind']['speed']
        sunrise_timetamp = datetime.datetime.fromtimestamp(
            data['sys']['sunrise'])
        sunset_timetamp = datetime.datetime.fromtimestamp(
            data['sys']['sunset'])
        print(
            f'|***{datetime.datetime.now().strftime("%Y-%m-%d %H:%M")}***|\n'
            f'Погода в городе {city}\nТемпература: {weather}°C\nВлажность: {humidity}%\n'
            f'Давление: {pressure}мм рт.ст\nВетер: {wind_speed} м/с\n'
            f'Восход солнца: {sunrise_timetamp}\n'
            f'Закат солнца: {sunset_timetamp}\n'
            f'Хорошего дня!!!!')

    except Exception as ex:
        print(ex)
        print('check name of city!!!!')


def main():
    city = input('Введите город: ')
    get_weather(city, open_weather_token)


if __name__ == '__main__':
    main()
