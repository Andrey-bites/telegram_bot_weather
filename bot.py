import requests
import datetime
from aiogram.dispatcher import Dispatcher

from aiogram.utils import executor
from aiogram import Bot, types

from config import bot_token, open_weather_token
import os
import sys
sys.path.append(os.path.dirname(__file__))

bot = Bot(token=bot_token)
dp = Dispatcher(bot)


@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    await message.reply('Привет я метеобот\nНапиши мне город и я пришлю сводку погоды!!')

@dp.message_handler()
async def get_weather(message: types.Message):

    code_to_smile = {
        "Clear": "Ясно \U00002600",
        "Clouds": "Облачно \U00002601",
        "Rain": "Дождь \U00002614",
        "Drizzle": "Дождь \U00002614",
        "Thunderstorm": "Гроза \U000026A1",
        "Snow": "Снег \U0001F328",
        "Mist": "Туман \U0001F32B"
    }

    try:
        request = requests.get(
            f'https://api.openweathermap.org/data/2.5/weather?q={message.text}&appid={open_weather_token}&units=metric')
        data = request.json()

        city = data['name']
        weather = data['main']['temp']
        weather_description = data["weather"][0]["main"]
        if weather_description in code_to_smile:
            wd = code_to_smile[weather_description]
        else:
            wd = "Посмотри в окно, не пойму что там за погода!"
        humidity = data['main']['humidity']
        pressure = data['main']['pressure']
        wind_speed = data['wind']['speed']
        sunrise_timetamp = datetime.datetime.fromtimestamp(
            data['sys']['sunrise'])
        sunset_timetamp = datetime.datetime.fromtimestamp(
            data['sys']['sunset'])
        await message.reply(
            f'|***{datetime.datetime.now().strftime("%Y-%m-%d %H:%M")}***|\n'
            f'Погода в городе {city}\nТемпература: {weather}°C {wd}\nВлажность: {humidity}%\n'
            f'Давление: {pressure}мм рт.ст\nВетер: {wind_speed} м/с\n'
            f'Восход солнца: {sunrise_timetamp}\n'
            f'Закат солнца: {sunset_timetamp}\n'
            f'Хорошего дня!!!!')

    except:
        await message.reply('\U00002620 |_Название города на английском языке_| \U00002620')


if __name__ == '__main__':
    executor.start_polling(dp)
