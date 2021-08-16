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
n_groups = 4
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
