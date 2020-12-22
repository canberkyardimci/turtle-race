import turtle
from turtle import Turtle
import time
import random
from random import randint


speed1 = random.randint(1,6)
speed2 = random.randint(1,6)
speed3 = random.randint(1,6)
speed4 = random.randint(1,6)
speed5 = random.randint(1,6)
print(speed1,speed2,speed3,speed4,speed5)

#Borders
border_pen = turtle.Turtle()
border_pen.color("white")
border_pen.penup()
border_pen.speed(0)
border_pen.setposition(-300, -300)
border_pen.pendown()
border_pen.pensize(3)
for side in range(4):
    border_pen.fd(500)
    border_pen.lt(90)
border_pen.hideturtle()

turtle.register_shape("finish.gif")

#Window Set-up
wn = turtle.Screen()
wn.title("Turtle Race")
wn.bgcolor("green")
wn.setup(width=700, height=400)

#Player Red
r_turtle = turtle.Turtle()
r_turtle.penup()
r_turtle.setposition(-250, 90)
r_turtle.speed(0)
r_turtle.shape("turtle")
r_turtle.color("red")

#Player Yellow
y_turtle = turtle.Turtle()
y_turtle.penup()
y_turtle.setposition(-250, 60)
y_turtle.speed(0)
y_turtle.shape("turtle")
y_turtle.color("yellow")

#Player Blue
b_turtle = turtle.Turtle()
b_turtle.penup()
b_turtle.setposition(-250, 30)
b_turtle.speed(0)
b_turtle.shape("turtle")
b_turtle.color("blue")


#Player Purple
w_turtle = turtle.Turtle()
w_turtle.penup()
w_turtle.setposition(-250, 0)
w_turtle.speed(0)
w_turtle.shape("turtle")
w_turtle.color("white")



#Player Black
black_turtle = turtle.Turtle()
black_turtle.penup()
black_turtle.setposition(-250, -30)
black_turtle.speed(0)
black_turtle.shape("turtle")
black_turtle.color("black")

#Finish Line
finish = turtle.Turtle()
finish.penup()
finish.speed(0)
finish.shape("finish.gif")
finish.setposition(250, 20)

#Finish Line 2
finish2 = turtle.Turtle()
finish2.penup()
finish2.speed(0)
finish2.shape("finish.gif")
finish2.setposition(250,79)
#Finish Line 3
finish3 = turtle.Turtle()
finish3.penup()
finish3.speed(0)
finish3.shape("finish.gif")
finish3.setposition(250,-29)

#Colors
color = ["red", "yellow", "blue", "white", "black"]


#Winner
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.setposition(-100, 0)
score_pen.hideturtle()

#Direction
def move_right():
    x = r_turtle.xcor()
    x += speed1
    r_turtle.setx(x)


def move_right():
    x = y_turtle.xcor()
    x += speed2
    y_turtle.setx(x)

def move_right():
    x = b_turtle.xcor()
    x += speed3
    b_turtle.setx(x)

def move_right():
    x = w_turtle.xcor()
    x += speed5
    w_turtle.setx(x)

def move_right():
    x = black_turtle.xcor()
    x += speed4
    black_turtle.setx(x)

def winner_table():
    x = 250




#Main loop
while True:
    wn.update()


    #Turtle Move
    if r_turtle.xcor() < 250:
        r_turtle.penup()
        x = r_turtle.xcor()
        x += speed1
        r_turtle.setx(x + speed1)

        # Turtle Move
    if y_turtle.xcor() < 250:
        y_turtle.penup()
        x = y_turtle.xcor()
        x += speed2
        y_turtle.setx(x + speed2)

        # Turtle Move
    if b_turtle.xcor() < 250:
        b_turtle.penup()
        x = b_turtle.xcor()
        x += speed3
        b_turtle.setx(x + speed3)

        # Turtle Move
    if w_turtle.xcor() < 250:
        x = w_turtle.xcor()
        x += speed4
        w_turtle.setx(x + speed4)

        # Turtle Move
    if black_turtle.xcor() < 250:
        black_turtle.penup()
        x = black_turtle.xcor()
        x += speed5
        black_turtle.setx(x + speed5)

    if r_turtle.xcor() > 200:
        score_pen.color("red")
        score_pen.write("Winner is: Red", align="left", font=("Arial", 20, "bold"))
        score_pen.setposition(-100, 0)
        break

    if y_turtle.xcor() > 200:
        score_pen.color("yellow")
        score_pen.write("Winner is: Yellow", align="left", font=("Arial", 20, "bold"))
        score_pen.setposition(-100, 0)
        break

    if b_turtle.xcor() > 200:
        score_pen.color("blue")
        score_pen.write("Winner is: Blue", align="left", font=("Arial", 20, "bold"))
        score_pen.setposition(-100, 0)
        break

    if w_turtle.xcor() > 200:
        score_pen.color("white")
        score_pen.write("Winner is: White", align="left", font=("Arial", 20, "bold"))
        score_pen.setposition(-100, 0)
        break

    if black_turtle.xcor() > 200:
        score_pen.color("black")
        score_pen.write("Winner is: Black", align="left", font=("Arial", 20, "bold"))
        score_pen.setposition(-100, 0)
        break



wn.mainloop()
