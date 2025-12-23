from turtle import Turtle,Screen
timm=Turtle()
timm.shape("turtle")
timm.color("red")
for i in range(10):
    timm.penup()
    timm.forward(10)
    timm.down()
    timm.forward(10)
screen=Screen()
screen.exitonclick()