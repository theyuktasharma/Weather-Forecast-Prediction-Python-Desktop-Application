import tkinter as tk
from tkinter import *
import requests
from pprint import pprint
from tkinter import Tk, Frame, BOTH
import tkinter
from PIL import Image, ImageTk
from gtts import gTTS
import requests
from pprint import pprint
from decimal import Decimal

root = tk.Tk()
L3 = Label(root, text="City",font="Helvetica 10 bold")
L3.pack(side=LEFT)
L3.place(x=100,y=150)

city=StringVar()

E3 = Entry(root, bd =5, textvariable=city)
E3.pack(side = LEFT)
E3.place(x=250,y=150)

#condition list which are good for travelling
best_conditions = {"GT":27,
                   "GW":"clear sky",
                   "HD":55}

#empty list will contains the score of each day from which we will get the highest value that will give us the index and that index + 1 will give us the day number

list_counter = []
counter = 0
def doit3():
        fo2=open("f.txt","w")
        global counter
        url = r'https://api.openweathermap.org/data/2.5/forecast?q={}&appid=b5473a745c4f03efeac0b648b695df24'.format(city.get())
        res = requests.get(url)
        data = res.json()
        index = 0
        max = 0
        for i in range(1):
            if(data["list"][i]["weather"][0]["description"] == best_conditions["GW"]):
                counter = counter + 1
            if(data["list"][i]["main"]["temp"]- 273 - best_conditions["GT"] <= 4 and data["list"][i]["main"]["temp"]- 273 - best_conditions["GT"] >= -4):
                counter  = counter + 1
            list_counter.append(counter)
            counter = 0
        for i in list_counter:
            if(i > max):
                max = i
            index = list_counter.index(max)
            
#checking the best day or the best condition for visiting the city in the next 5 days            
        for j in list_counter:
            if (max == j):
                print("Day %s is a good day to visit where weather conditions are %s \n Temperature : %s C \n Maximum Temperature : %s C \n Minimum Temperature : %s C " %(str(list_counter.index(j) + 1),
                                                                                              data["list"][list_counter.index(max)]["weather"][0]["description"],
                                                                                              round(Decimal(data["list"][list_counter.index(j)]["main"]["temp"] - 273),2),
                                                                                              round(Decimal(data["list"][list_counter.index(j)]["main"]["temp_min"] - 273) , 2),
                                                                                              round(Decimal(data["list"][list_counter.index(j)]["main"]["temp_max"] - 273),2)), file=fo2)
        fo2.close()
        f=open("f.txt","r")
        content2=f.read()
        label3=Label(root, text=content2, font="Helvetica 10 italic")
        label3.pack()
        label3.place(x=450,y=300)
        
sub2=Button(root, text="GO", command=doit3)
sub2.pack(side=LEFT)
sub2.place(x=400,y=150)

root.mainloop()           
