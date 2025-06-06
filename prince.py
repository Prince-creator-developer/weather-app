from tkinter import Tk, StringVar, Label, Entry, Button, Text, INSERT
import requests
import json
from datetime import datetime
 
#Initialize Window

root =Tk()
root.geometry("400x400") #size of the window by default
root.resizable(0,0) #to make the window size fixed
#title of our window
root.title("Weather App - BNMIT")
weather_now = Label(root, text = "The Weather is:", font = 'arial 12 bold').pack(pady=10) 
tfield = Text(root, width=46, height=10)
tfield.pack() 

# ----------------------Functions to fetch and display weather info
city_value = StringVar()
def time_format_for_location(utc_with_tz, timezone_offset):
    local_time = datetime.utcfromtimestamp(utc_with_tz + timezone_offset)
    return local_time.strftime('%Y-%m-%d %H:%M:%S')  # Shows date and time

   
 
def showWeather():
    #Enter you api key, copies from the OpenWeatherMap dashboard
    api_key = "8ef2824bdbf254050f41cb13ee62d0c1"
      #sample API 
 
    # Get city name from user from the input field (later in the code)
    city_name=city_value.get()
 
    # API url
    weather_url = 'http://api.openweathermap.org/data/2.5/weather?q=' + city_name + '&appid='+api_key
 
    # Get the response from fetched url
    response = requests.get(weather_url)
 
    # changing response from json to python readable 
    weather_info = response.json()
 
 
    tfield.delete("1.0", "end")   #to clear the text field for every new output
 #as per API documentation, if the cod is 200, it means that weather data was successfully fetched
 
 
    if weather_info['cod'] == 200:
         # value of kelvin is 273.15
 
#-----------Storing the fetched values of weather of a city
 
        temp = int(weather_info['main']['temp'] - 273.15)                                     #converting default kelvin value to Celcius
        feels_like_temp = int(weather_info['main']['feels_like'] - 273.15)
        pressure = weather_info['main']['pressure']
        humidity = weather_info['main']['humidity']
        wind_speed = weather_info['wind']['speed'] * 3.6
        sunrise = weather_info['sys']['sunrise']
        sunset = weather_info['sys']['sunset']
        timezone = weather_info['timezone']
        cloudy = weather_info['clouds']['all']
        description = weather_info['weather'][0]['description']
 
        sunrise_time = time_format_for_location(sunrise,timezone)
        sunset_time = time_format_for_location(sunset,timezone)
 
#assigning Values to our weather varaible, to display as output
        city_name = weather_info['name'] + ', ' + weather_info['sys']['country']
        weather = f"\nWeather of: {city_name}\nTemperature (Celsius): {temp}°\nFeels like in (Celsius): {feels_like_temp}°\nWind-speed (in km/hr):{wind_speed}\nPressure: {pressure} hPa\nHumidity: {humidity}%\nSunrise at {sunrise_time}\nSunset at {sunset_time}\nCloud: {cloudy}%\nTime-zone:{timezone}\nInfo: {description}"
    else:
        weather = f"\n\tWeather for '{city_name}' not found!\n\tKindly Enter valid City Name !!"
 
 
 
    tfield.insert(INSERT, weather)   #to insert or send value in our Text Field to display output
 
 
 
#------------------------------Frontend part of code - Interface
 
 
city_head= Label(root, text = 'Enter City Name', font = 'Arial 12 bold').pack(pady=10) #to generate label heading
 
inp_city = Entry(root, textvariable = city_value,  width = 24, font='Arial 14 bold',bg="orange").pack()
 
 
Button(root, command = showWeather, text = "Check Weather", font="Arial 10", bg='lightblue', fg='black', activebackground="teal", padx=5, pady=5 ).pack(pady= 20)
 
#to show output
 

 

root.mainloop()

