import requests
import ctypes
import os
import urllib
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
#from tkinter import messagebox


def WeatherData(city):
    #The API call is different for different accounts
    responce = requests.get("http://api.openweathermap.org/data/2.5/weather?q=" + city + "&APPID=eb820c62182f83ffae8b2129055f70c8")
    converted = responce.json()
    return(converted)

def GetResolution():
    user32 = ctypes.windll.user32
    #The number 78 is for the screen width and 79 is for the height
    resolution = str(user32.GetSystemMetrics(78)) + "x" + str(user32.GetSystemMetrics(79))
    return(resolution)

def GetImg(key, resolution):
    types = {200: "thunderstorm", 201: "thunderstorm", 202: "thunderstorm", 210: "thunderstorm", 211: "thunderstorm", 212: "thunderstorm", 221: "thunderstorm", 230: "thunderstorm", 231: "thunderstorm", 232: "thunderstorm",
         300: "drizzle", 301: "drizzle", 302: "drizzle", 310: "drizzle", 311: "drizzle", 312: "drizzle", 313: "drizzle", 314: "drizzle", 321: "drizzle",
         500: "rain", 501: "rain", 502: "rain", 503: "rain", 504: "rain", 511: "rain", 520: "rain", 521: "rain", 522: "rain", 531: "rain",
         600: "snow", 601: "snow", 602: "snow", 611: "snow", 612: "snow", 615: "snow", 616: "snow", 620: "snow", 621: "snow", 622: "snow",
         701: "mist", 711: "smoke", 721: "haze", 731: "whirls", 741: "fog", 751: "sand", 761: "dust", 771: "squalls", 781: "tornado",
         800: "clear", 801: "clouds", 802: "clouds", 803: "clouds", 804: "clouds"}
    weather = types[key]
    url = "https://source.unsplash.com/" + resolution + "/?" + weather
    d = urllib.request.urlopen(url)
    #print(d.info()["Content-Length"])
    urllib.request.urlretrieve(url, "W.jpg")

def SetWallpaper():
    location = os.getcwd()
    path = os.path.normpath(location + "/W.jpg")
    #The number 20 indicates the action of changing the wallpaper
    SPI_SET_WALLPAPER = 20
    ctypes.windll.user32.SystemParametersInfoW(SPI_SET_WALLPAPER, 0, path, 0)

#city = input("City: ")


#This is the position of the current weather info in the data
def change():
    city = nimi.get()
    data = WeatherData(city)
    key = data["weather"][0]["id"]
    resolution = GetResolution()
    GetImg(key, resolution)
    SetWallpaper()
    raam.destroy()



raam = Tk()
raam.title("WallChanger")
raam.geometry("300x100")

nimi = ttk.Entry(raam)
nimi.grid(column = 0, row = 1, padx = 10, pady = 0, sticky = (N))

tekst = ttk.Label(raam, text = "Sisestage linna nimi (Inglise keeles)")
tekst.grid(column = 0, row = 0, padx = 20, pady = 0, sticky = (N))

nupp = ttk.Button(raam, text="Vaheta", command=change)
nupp.grid(column = 0, row = 2, padx = 100, pady = 0, sticky = (N))

raam.columnconfigure(0, weight = 1)
raam.rowconfigure(0, weight = 1)
raam.rowconfigure(1, weight = 1)
raam.rowconfigure(2, weight = 1)

rb = ImageTk.PhotoImage(Image.open("./rainbow_45.png"))
sun = ImageTk.PhotoImage(Image.open("./sun_45.png"))
Label(raam, image = rb).place(x = 10, y = 30, width = 50)
Label(raam, image = sun).place(x = 240, y = 30)

raam.mainloop()


