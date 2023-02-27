import turtle as a
import random

ant = a.Turtle()
a.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


ant.speed("fastest")


def draw_spirograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        ant.color(random_color())
        ant.circle(100)
        current_heading = ant.heading()
        ant.setheading(current_heading + size_of_gap)


draw_spirograph(10)


screen = a.Screen()
screen.exitonclick()
