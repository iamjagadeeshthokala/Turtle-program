import turtle
import random

def random_color():
    return (random.random(), random.random(), random.random())

turtle.speed(0)

for _ in range(100):
    turtle.color(random_color())
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.right(10)

turtle.done()
