import math 
import turtle



def polyline(t, n, lenght, angle):
    """
        Desenha n segmentos de reta com comprimentos dado o angulo (em graus) entre eles, t é um turtle 
    """
    for i in range(n):
        t.fd(lenght)
        t.lt(angle)
        

def polygon(t, n, length):
    angle = 360 / n 
    polyline(t, n, length, angle)


def arc(t, r, angle):
    arc_length =  2 * math.pi * r * angle / 360
    n = int(arc_length / 3 ) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n
    polyline(t, n, lenght=step_length, angle=step_angle)
    

def circle(t, r):
    arc(t, r, 360)


circle()