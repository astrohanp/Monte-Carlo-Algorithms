from visual import *
from visual.graph import *
import random
import math

random.seed(None) #Seed generator, None=>System Clock
jmax = 1000
x = 0.0; y = 0.0 ; K = 31

graph1 = gdisplay(width=500,height = 500,title = 'Random Walk', xtitle ='x', ytitle = 'y')

pts1 = gcurve(color = color.yellow)
pts2 = gcurve(color = color.red)
pts3 = gcurve(color = color.cyan)
pts4 = gcurve(color = color.green)
pts5 = gcurve(color = color.blue)
curve_seq = [pts1,pts2,pts3,pts4,pts5]
R_sqr = []

for i in range(0,K):
    random.seed(None) #Seed generator, None=>System Clock
    pts = random.choice(curve_seq)
    for j in range(0,jmax+1):
        pts.plot(pos = (x,y))
        x += (random.random()-0.5)*2                    #-1=<x=<1
        y += (random.random()-0.5)*2                    #-1=<y=<1
        x1 = x/math.sqrt((x*x)+(y*y))
        y1 = y/math.sqrt((x*x)+(y*y))
        pts.plot(pos = (x1,y1))
        rate(1000)
    print i," ",((x*x)+(y*y))
    R_sqr.append((x*x)+(y*y))                 #Mean Square Distance for this Trial

R = 0.0

for i in range(0,K):                          #Calculating the average R square for K trials
    R = R+R_sqr[i]
    #print R

R_avg = R/K

print "Average value of R squares for K trials = ", R_avg

