import ctypes
import os
import sys
#import random
#import time
import requests

BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
API_KEY = " "
CITY = " "

url = BASE_URL + "appid=" + API_KEY + "&q=" + CITY

response = requests.get(url).json()

print(response)
icon = response['weather'][0]['icon']
print(icon)

class Main:
    def __init__(self):

        #now=time.strftime("%H:%M:%S")
        #print("The current date and time is",now)
        #if(now > '18:00:00'):
        #    print("<")
        self.path=os.path.abspath(os.path.dirname(sys.argv[0]))
        for root, directories, files in os.walk(os.path.join(self.path, 'backgrounds')):
            self.backgrounds = [file.lower() for file in files if file.endswith(('.png', '.jpg', '.jpeg'))]
        img = self.path+"/backgrounds/" + icon + ".jpg"
        #print(self.path)
        if(img!=0):
            ctypes.windll.user32.SystemParametersInfoW(20, 0, img, 0)
        else:
            img = self.path + "/backgrounds/default.jpg"
            ctypes.windll.user32.SystemParametersInfoW(20, 0, img, 0)

application=Main()
