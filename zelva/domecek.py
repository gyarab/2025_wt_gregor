import turtle
import random
import math

t = turtle.Turtle()
t.speed(0)
t.width(2)

def domecek(a):
    s = math.sqrt(2) * a / 2
    t.forward(a)
    t.right(90)
    t.forward(a)
    t.right(45)
    t.forward(s)
    t.right(90)
    t.forward(s)
    t.right(45)
    t.forward(a)
    t.right(90)
    t.forward(a)
    t.right(90)

polomer = 150
pocet_domecku = 12

t.penup()
t.goto(0, -polomer)
t.pendown()
t.setheading(0)

for i in range(pocet_domecku):
    velikost = random.randint(30, 60)
    t.penup()
    t.forward(polomer)
    t.pendown()
    t.setheading(360 / pocet_domecku * i)
    domecek(velikost)
    t.penup()
    t.setheading(360 / pocet_domecku * (i + 1))
    t.forward(-polomer)
    t.pendown()

turtle.done()
