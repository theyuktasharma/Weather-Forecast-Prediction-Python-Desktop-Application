import tkinter as tk
from tkinter import Entry, IntVar
from tkinter import *
from gtts import gTTS
import requests
from pprint import pprint
from tkinter import Tk, Frame, BOTH
import tkinter
from PIL import Image, ImageTk
from decimal import Decimal
import re

root = tk.Tk()
root.geometry("1000x500+300+300")

#BACKGROUND IMAGE
im = Image.open('w5.jpg')
tkimage = ImageTk.PhotoImage(im)
myvar=tkinter.Label(root,image = tkimage)
myvar.place(x=0, y=0, relwidth=1, relheight=1)


#TEXTS
w = tk.Label(root, text="WEATHER FORECAST", fg="White", bg="Black", font="Helvetica 40 bold italic")
w.pack()
w.place(x=250,y=20)

    
#INPUT ENTRY
L1 = Label(root, text="Enter City Name",font="Helvetica 10 bold")
L1.pack(side=LEFT)
L1.place(x=100,y=100)


city=StringVar()

E1 = Entry(root, bd =5, textvariable=city)
E1.pack(side = LEFT)
E1.place(x=250,y=100)



def doit():
    
    fo = open("d.txt", "w")
    url = r'https://api.openweathermap.org/data/2.5/weather?q={}&appid=b5473a745c4f03efeac0b648b695df24'.format(str(city.get()))

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
    d=open("d.txt","r")
    content=d.read()
    label1=Label(root,text=content,font="Helvetica 10 italic")
    label1.pack()
    label1.place(x=100,y=300)
    text=''
    with open("d.txt", "r") as file:
        for line in file:
            text=text+ line



    speech=gTTS(text)
    speech.save("d.mp3")

    from pygame import mixer # Load the required library
    mixer.init()
    mixer.music.load('C:/Users/Pract/Desktop/Study Material/Computer Science/Semester-II/Data Structures Project-2019/d.mp3')
    mixer.music.play()
    
sub1=Button(root, text="GO", command=doit)
sub1.pack(side=LEFT)
sub1.place(x=400,y=100)

############################################################################
L2 = Label(root, text="Number of Days",font="Helvetica 10 bold")
L2.pack(side=LEFT)
L2.place(x=100,y=150)

days=tk.IntVar()

E2 = Entry(root, bd =5, textvariable=days)
E2.pack(side = LEFT)
E2.place(x=250,y=150)

def doit2():
    fo1=open("max.txt", "w")
    go=open("min.txt", "w")
    if (days.get() in range(0, 5)):
        url = r'https://api.openweathermap.org/data/2.5/forecast?q={}&appid=b5473a745c4f03efeac0b648b695df24'.format(city.get())
        res = requests.get(url)
        data = res.json()
        for i in range(0, days.get()):
            #print("The temperature of %dth day is %f" % (i + 1, (Decimal(data['list'][i]['main']['temp'] - 273))),file=fo1)
            
            print("The minimum temperature of %dth day is %f" % (i + 1, (Decimal(data['list'][i]['main']['temp_min'] - 273))),file=go)
            print("The maximum temperature of %dth day is %f" % (i + 1, (Decimal(data['list'][i]['main']['temp_max'] - 273))),file=fo1)
            #print("The weather discription of %sth day is %s" % (i + 1, (data['list'][i]['weather'][0]["description"])),file=fo1)
    else:
            print("ERROR\n We can only provide you data of atmost 5 days.", file=fo1)

    fo1.close()
    go.close()
    #string to file save

    #Maximum Temperature


    file = open('max.txt', 'r')

    file = file.read()

    numbers = re.findall(r"[-+]?\d*\.\d+|\d+", file)


    new=[]
    for i in numbers[1::2]:
        new.append(float(i))
    numbers=new
    g1=open("gmax.txt","w")
    print(numbers,file=g1)
    g1.close()

        

    #Minimum Temperature
    file = open('min.txt', 'r')

    file = file.read()

    numbers = re.findall(r"[-+]?\d*\.\d+|\d+", file)




    new=[]
    for i in numbers[1::2]:
        new.append(float(i))
    numbers=new

    g2=open("gmin.txt","w")
    print(numbers,file=g2)
    g2.close()

    #graph
    import numpy as np
    import matplotlib.pyplot as plt
    r1=open("gmax.txt","r")
    a=r1.read()
    z=a.split(",")
    print(z)

    #Converts list encased as a string directly to a proper list with int values
    def string_to_List(string):
     temp_li=string.split(',')
     for i in range(0,len(temp_li)):
      if i==(len(temp_li)-1):
       temp_li[i]=temp_li[i][1:len(temp_li[i])-3]
      else:
       temp_li[i]=temp_li[i][1:]
      temp_li[i]=float(temp_li[i])
     return temp_li 
        

    #s=np.asarray(a)
    #print(s)
    #r1.close()
    r2=open("gmin.txt","r")
    b=r2.read()
    #t=np.asarray(b)
    #print(t)
    #r2.close()

    # data to plot
    n_groups = days.get()
    means_frank = string_to_List(a)
    r1.close()
    means_guido = string_to_List(b)
    r2.close()

    # create plot
    index = np.arange(n_groups)
    bar_width = 0.35
    opacity = 0.8

    rects1 = plt.bar(index, means_frank, bar_width,
    alpha=opacity,
    color='b',
    label='MAX TEMP')

    rects2 = plt.bar(index + bar_width, means_guido, bar_width,
    alpha=opacity,
    color='g',
    label='MIN TEMP')

    plt.xlabel('DAYS')
    plt.ylabel('TEMPERATURE')
    plt.title('MAX & MIN TEMPERATURES')
    plt.xticks(index + bar_width, ('DAY1', 'DAY2', 'DAY3', 'DAY4'))
    plt.legend()

    plt.tight_layout()
    plt.show()


    #e=open("e.txt","r")
    #content1=e.read()
    #label2=Label(root,text=content1,font="Helvetica 10 italic")
    #label2.pack()
    #label2.place(x=300,y=300)

sub2=Button(root, text="GO", command=doit2)
sub2.pack(side=LEFT)
sub2.place(x=400,y=150)

#############################################################

L3 = Label(root, text="Best days to visit \n in next 5 days",font="Helvetica 10 bold")
L3.pack(side=LEFT)
L3.place(x=100,y=200)


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
        label3.place(x=300,y=300)
        
sub3=Button(root, text="GO", command=doit3)
sub3.pack(side=LEFT)
sub3.place(x=250,y=200)



root.mainloop()

