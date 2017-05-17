import turtle

num_diamonds = 40
angle_rotation = 360/num_diamonds

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

def draw_square(name):
    for i in range(4):
        name.forward(100)
        name.right(90)

def draw_circle(name):
    name.circle(100)

def draw_triangle(name):
    name.forward(100)
    name.left(120)
    name.forward(100)
    name.left(110)
    name.forward(110)
    name.left(130)
    name.forward(50)

def draw_diamond(name):
    name.left(15)
    name.forward(100)
    name.right(30)
    name.forward(100)
    name.right(150)
    name.forward(100)
    name.right(30)
    name.forward(100)
    name.right(165)

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

print "Creating Screen"
window = create_screen("black")
name = create_turtle_object("bill", "arrow", "blue", 8)

#draw a circle from squares
# for i in range(36):
#     draw_square(name)
#     name.right(10)

#draw a flower
for i in range(1, num_diamonds + 1):
    draw_diamond(name)
    name.right(angle_rotation)
name.right(90)
name.forward(400)
# window.exitonclick()

# triforce(name, 200, 1, 0)
window.exitonclick()
