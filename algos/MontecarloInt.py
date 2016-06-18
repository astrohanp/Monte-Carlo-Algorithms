from matplotlib import pyplot as plt
import numpy as np
import math
import random

#Calculating the integration of sin(x) from 0 to pi
b=math.pi
a=0
x = np.linspace(a,b,1000)
y = np.sin(x)


#Initializing constants
n1 = 10
n2 = 100
x_a = []
fx_a = []
avg1 = 0.0
avg2 = 0.0
variance1 = 0.0

#Without any variance reduction technique with sample size = 10

for i in range(n1):
    t = random.uniform(a,b)
    ft = math.sin(t)
    plt.plot([t,t],[0,ft])
    avg1 = avg1+ft
    variance1 = variance1 + ((ft-2)*(ft-2))

avg1 = ((b-a)*avg1)/n1
variance1 = variance1/n1
print variance1
plt.plot(x,y,label='sin(x)', color='c')
plt.title('Estimation of integration of sin(x) \n Actual value = 2 \n Calculated value(with n= 10)= %s' %avg1)
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.show()

#Without any variance reduction technique with sample size = 100

for i in range(n2):
    t = random.uniform(a,b)
    ft = math.sin(t)
    plt.plot([t,t],[0,ft])
    avg2 = avg2+ft

avg2 = ((b-a)*avg2)/n2
plt.plot(x,y,label='sin(x)', color='c')
plt.title('Estimation of integration of sin(x) \n Actual value = 2 \n Calculated value(with n= 100)= %s' %avg2)
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.show()


#Using Adaptive Sampling
variance = 10
while(variance>2.02 or variance<2.00):
    variance = 0.0
    avg3 = 0.0
    x1 = []
    fx1 = []
    for i in range(n1):
        t = random.uniform(a,b)
        ft = math.sin(t)
        avg3 = avg3+ft
        x1.append(t)
        fx1.append(ft)

    avg3 = ((b-a)*avg3)/n1
    for i in fx1:
        variance = variance+((i-avg3)*(i-avg3))
    variance = variance/n1
    print variance,"  ",avg3
    x_a = x1;fx_a= fx1
    

for i in range(0,len(x_a)):
    plt.plot([x_a[i],x_a[i]],[0,fx_a[i]])
plt.plot(x,y,label='sin(x)', color='c')
plt.title('Estimation of integration of sin(x) \n Actual value = 2 \n Calculated value(with n= 10[adp. sampling])= %s' %avg3)
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.show()






