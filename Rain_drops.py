#Estimation of value of pi using raindrops
from matplotlib import pyplot as plt
import math
import random

r = 0.5;drops = 10000;

number_of_drops_in_circle = 0
drops_in_circle_x = []
drops_in_circle_y = []
drops_not_x = []
drops_not_y = []
for i in range(drops):
    x = (random.random())
    y = (random.random())
    p = math.sqrt(((x-0.5)*(x-0.5))+((y-0.5)*(y-0.5)))
    if p<=r:
        drops_in_circle_x.append(x)
        drops_in_circle_y.append(y)
        number_of_drops_in_circle += 1
    else:
        drops_not_x.append(x)
        drops_not_y.append(y)
drops = 10000.0
pi = ((4*number_of_drops_in_circle)/drops)

x1=[0,0,1.0,1.0,0]
y1=[0,1.0,1.0,0,0]
plt.plot(x1,y1,color = 'g',linewidth=2.0)
plt.scatter(drops_in_circle_x,drops_in_circle_y,label='Drops inside the circle',color ='b')
plt.scatter(drops_not_x,drops_not_y,label='Drops outside the circle',color ='r')
plt.ylabel("Number of Drops = %s" %drops)
plt.title("Estimation of pi = %s" %pi)
plt.legend()
plt.show()

