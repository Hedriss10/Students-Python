import math 
import turtle



def polyline(t, n, lenght, angle):
    for i in range(n):
        t.fd(lenght)
        t.lt(angle)