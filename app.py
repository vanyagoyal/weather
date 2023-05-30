from tkinter import *
import requests
import json

root=Tk()
root.title("My Weather App")
root.geometry("350x300")
root.overrideredirect(True)

root.configure(background="white")
#Setting labels
city_name_label=Label(root, text="City Name",font=("Helvetica", 18,'bold'),bg="white")
city_name_label.place(relx=0.28,rely=0.15,anchor=CENTER)

city_entry=Entry(root)
city_entry.place(relx=0.28,rely=0.35,anchor=CENTER)

weather_info_label = Label(root,text="Weather: ", bg="white", font=("bold", 10))
weather_info_label.place(relx=0.23,rely=0.6,anchor=CENTER) 

humidity_info_label = Label(root,text="Humidity: ", bg="white", font=( "bold",10)) 
humidity_info_label.place(relx=0.22,rely=0.7,anchor=CENTER) 

def city_weather() :
    city_name_label['text'] = city_entry.get()
    api_requests = requests.get("https://api.openweathermap.org/data/2.5/weather?q=" + city_entry.get() + "&appid=" + "21cab08deb7b27f4c2b55f3e2df28ea4")
    output = json.loads(api_requests.content)
    
    weather_info = output['weather'][0]['main']
    print(weather_info)
    weather_info_label['text'] = "Weather : " + str(weather_info)
    
    humidity = output['main']['humidity']
    print(str(humidity) + "%")
    humidity_info_label['text'] = "Humidity : " + str(humidity) + "%"

btn = Button(root , text="Get Information" , relief = FLAT , command = city_weather)
btn.place(relx=0.5 , rely = 0.8 , anchor = CENTER)

root.mainloop()