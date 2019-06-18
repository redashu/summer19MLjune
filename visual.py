#!/usr/bin/python3

import  matplotlib.pyplot    as   plt
#   only  loading  python ori  lib 
x=[2,3]
x1=[4,3,8]
y1=[2,9,7]
y=[9,5]

plt.xlabel("time")
plt.ylabel("speed")
plt.plot(x,y,label="water")   #   this will draw a straight  line 
plt.plot(x1,y1,label="sand")   #   this will draw a straight  line 
plt.bar(x,y)   #   to plot bar  graphs 
plt.bar(x1,y1)   #   to plot bar  graphs 
plt.grid(color='green')  #  to form  grid  in graph 
plt.legend() #   to show labels with plot  
plt.xlim(0,12)  #  to show  min and max  number in x  axis 
plt.ylim(0,15)   #   y axis
plt.show()

