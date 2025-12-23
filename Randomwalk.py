import turtle as t
import random
timm=t.Turtle()
colours=["red","brown","green","pink","black","orange","yellow","purple","blue","violet"]
def move_forward():
    timm.forward(random.randint(10, 50))

def move_right():
    timm.right(random.randint(0, 90))

def move_left():
    timm.left(random.randint(0, 90))

def move_backward():
    timm.backward(random.randint(10, 50))

value = [move_forward, move_right, move_left, move_backward]

for _ in range(500):
    random.choice(value)()
    timm.color(random.choice(colours))
