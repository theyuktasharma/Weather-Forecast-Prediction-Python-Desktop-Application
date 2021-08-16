from gtts import gTTS
import requests
from pprint import pprint

city=str(input("enter name"))
fo = open("d.txt", "w")
url = r'https://api.openweathermap.org/data/2.5/weather?q={}&appid=b5473a745c4f03efeac0b648b695df24'.format(city)

res = requests.get(url)

data = res.json()

temp = data['main']['temp']
wind_speed = data['wind']['speed']
latitude = data['coord']['lat']
longitude = data['coord']['lon']
description = data['weather'][0]['description']
print('Temperature : {}'.format(temp), file=fo)
print('Wind Speed : {}m/s'.format(wind_speed), file=fo)
print('Latitude : {}'.format(latitude), file=fo)
print('Longitude : {}'.format(longitude), file=fo)
print('Description : {}'.format(description), file=fo)

fo.close()

text=''
with open("d.txt", "r") as file:
    for line in file:
        text=text+ line



speech=gTTS(text)
speech.save("d.mp3")

from pygame import mixer # Load the required library
mixer.init()
mixer.music.load('C:/Users/Pract/Desktop/d.mp3')
mixer.music.play()

