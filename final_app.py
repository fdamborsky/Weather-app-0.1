from tkinter import *
import customtkinter
import requests
from PIL import Image,ImageTk
import pywinstyles,pywinstyles
from dictionary import dictionary

# - WINDOW SETTINGS
window = customtkinter.CTk()
window.geometry("540x700")
window.title("Weather app")
window.resizable(False,False)
window.iconbitmap("images/icon.ico")
pywinstyles.apply_style(window,"optimised")
pywinstyles.change_header_color(window, color="#fe672e")  

# - BACKGROUND
bg_image = customtkinter.CTkImage(Image.open("images/initial_image.jpg"),size=(540,960))
bg_label = customtkinter.CTkLabel(window,image=bg_image,text=())
bg_label.place(x=0,y=-70)

# - Settings
temperature = "-"
description = "..."
input_text = ""

# - REQUEST DETAILS
api_key = "your own api key"

# - FUNCTION    

def first_frame():
    def sec():
        # - GETTING DATA AND INFO
        input_text = user_entry2.get()
        user_entry2.delete(0,END)
        url = f"https://api.openweathermap.org/data/2.5/weather?q={input_text}&units=metric&APPID={api_key}"
        request = requests.get(url)
        data= request.json()
        temperature = round(data["main"]["temp"],1)
        description = data["weather"][0]["description"]

        # - CHANGE OF IMAGE
        for key in dictionary:
            if key == description:
                color_key = key
                result2 = dictionary[key][0]
        weather_image2 = customtkinter.CTkImage(Image.open(result2),size=(540,960))
        weather_image_label.configure(image = weather_image2)

        # - OTHER LABEL CHANGE
        temperature_label.configure(text=f"{temperature}°C")
        city_name.configure(text=(input_text.upper()))
        apply_button2.configure(fg_color=f"{dictionary[color_key][1]}",hover_color=f"{dictionary[color_key][2]}")

    # - GETTING DATAS
    input_text = user_entry.get()
    user_entry.delete(0,END)
    url = f"https://api.openweathermap.org/data/2.5/weather?q={input_text}&units=metric&APPID={api_key}"
    request = requests.get(url)
    data= request.json()

    # - TAKING IMPORTANT DATA
    temperature = round(data["main"]["temp"],1)
    description = data["weather"][0]["description"]

    # - FRAME CREATION
    frame = customtkinter.CTkFrame(window,height=960,width=540)
    frame.pack()

    # - IMAGE CHANGE
    for key in dictionary:
        if key == description:
            color_key = key
            result2 = dictionary[key][0]
    weather_image = customtkinter.CTkImage(Image.open(result2),size=(540,960))
    weather_image_label = customtkinter.CTkLabel(frame,image=weather_image,text=" ")
    pywinstyles.set_opacity(weather_image_label)
    weather_image_label.place(x=0,y=0)

    # - CITY NAME LABEL
    city_name = customtkinter.CTkLabel(frame,text=(input_text.upper()),font=("Proxima Nova Bl Pro",30),bg_color="#e0eff4",text_color="#434949")
    city_name.place(x=80,y=35)
    pywinstyles.set_opacity(city_name,color="#e0eff4")

    # - TEMPERATURE LABEL
    temperature_label = customtkinter.CTkLabel(frame,text=f"{temperature}°C",font=("Proxima Nova Bl Pro",140),bg_color="#e0eff4",text_color="white",width=540,anchor="center")
    #if temperature >= 10:
        #temperature_label.configure(font=("Proxima Nova Bl Pro",110))
    temperature_label.place(x=0,y=380)
    pywinstyles.set_opacity(temperature_label,color="#e0eff4")

    user_entry2 = customtkinter.CTkEntry(frame,font=("Proxima Nova Bl Pro",30),placeholder_text="Please enter city...",width=380,height=35,fg_color="white",corner_radius=15,border_width=1,border_color="white",bg_color="#fda158",text_color="grey")
    user_entry2.place(x=80,y=550)
    pywinstyles.set_opacity(user_entry2,color="#fda158") 

    # - Button
    apply_button2 = customtkinter.CTkButton(frame,font=("Proxima Nova Bl Pro",30),text="APPLY",width=380,height=30,fg_color=f"{dictionary[color_key][1]}",text_color="white",bg_color="#fda158",command=sec,hover_color=f"{dictionary[color_key][2]}")
    apply_button2.place(x=80,y=590)
    pywinstyles.set_opacity(apply_button2,color="#fda158")

# - User entry
user_entry = customtkinter.CTkEntry(window,font=("Proxima Nova Bl Pro",30),placeholder_text="Please enter city...",width=380,height=35,fg_color="white",corner_radius=15,border_width=1,border_color="white",bg_color="#fda158",text_color="grey")
user_entry.place(x=80,y=500)
pywinstyles.set_opacity(user_entry,color="#fda158") # just add this line

# - Button
apply_button = customtkinter.CTkButton(window,font=("Proxima Nova Bl Pro",30),text="APPLY",width=380,height=30,fg_color="#fe672e",text_color="white",bg_color="#fda158",command=first_frame,hover_color="#e84000")
apply_button.place(x=80,y=540)
pywinstyles.set_opacity(apply_button,color="#fda158")

# - MAIN LOOP
window.mainloop()
