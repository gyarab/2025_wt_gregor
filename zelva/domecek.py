from turtle import *
from math import sqrt

def domecek(a):
    forward(a)
    left(100)
    forward(a)
    left(150)
    forward(sqrt(2*a**2))
    right(150)
    forward(a)
    right(150)
    forward(sqrt(2*a**2))
    left(150)
    forward(a)
    left(100)
    forward(a)
    right(150)
    forward(sqrt(2*a**2)/2)
    right(100)
    forward(sqrt(2*a**2)/2)

domecek(100)
exitonclick()
