
#Maximum Temperature
import re

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

