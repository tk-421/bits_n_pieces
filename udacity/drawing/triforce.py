import turtle

def create_screen(color):
    window = turtle.Screen()
    window.bgcolor(color)
    return window

def create_turtle_object(name, shape, color, speed):
    name = turtle.Turtle()
    name.shape(shape)
    name.color(color)
    name.speed(speed)
    return name

def triforce(name, length, ori, recursion):
    recursion = recursion + 1
    name = name
    for i in range(0,3):
        if recursion < 4:
            name.forward(length/2)
            name.left(120)
            triforce(name, length/2, 0, recursion)
            name.right(120)
            name.forward(length/2)
        else:
            name.forward(length)
        if ori==1:
            name.left(120)
        else:
            name.right(120)

window = create_screen("black")
name = create_turtle_object("link", "arrow", "green", 8)
triforce(name, 200, 1, 0)
window.exitonclick()
