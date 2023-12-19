import turtle

def draw_star(size):
    for _ in range(5):
        turtle.forward(size)
        turtle.right(144)

def move_up():
    turtle.setheading(90)
    turtle.forward(10)

def move_down():
    turtle.setheading(270)
    turtle.forward(10)

def move_left():
    turtle.setheading(180)
    turtle.forward(10)

def move_right():
    turtle.setheading(0)
    turtle.forward(10)

def main():
    turtle.color("white")
    turtle.showturtle()

    turtle.speed(0)  # Set the turtle's speed to the fastest
    turtle.bgcolor("black")  # Set the background color to black

    # Set up the turtle's initial position
    turtle.penup()
    turtle.goto(-200, 200)
    turtle.pendown()

    # Draw multiple stars
    for i in range(5):
        draw_star(100)
        turtle.penup()
        turtle.forward(150)
        turtle.pendown()

    # Set up controls
    turtle.listen()
    turtle.onkey(move_up, "Up")
    turtle.onkey(move_down, "Down")
    turtle.onkey(move_left, "Left")
    turtle.onkey(move_right, "Right")


    turtle.done()

if __name__ == "__main__":
    main()
