from turtle import *

bgcolor("black")
pensize(2)
speed(0)

colors = ["red", "yellow", "green", "blue", "indigo", "violet", "cyan", "magenta"]

for y in colors:
    right(45)
    color(y)
    for x in range(8):
        forward(50)
        right(45)
done()
hideturtle()
