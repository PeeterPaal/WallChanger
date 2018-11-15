import requests
import json
import ctypes
import os

def WeatherData(city):
    #The API call is different for different accounts
    responce = requests.get("http://api.openweathermap.org/data/2.5/weather?q=" + city + "&APPID=eb820c62182f83ffae8b2129055f70c8")
    converted = responce.json()
    return(converted)

def SetWallpaper(img):
    location = os.getcwd()
    path = os.path.normpath(location + "/" + str(img) + ".jpg")
    #The number 20 indicates the action of changing the wallpaper
    SPI_SET_WALLPAPER = 20
    ctypes.windll.user32.SystemParametersInfoW(SPI_SET_WALLPAPER, 0, path, 0)

city = str(input("Input city name: "))
data = WeatherData(city)
index = str(data["weather"][0]["id"])
#print (index)
SetWallpaper(index)
