import random
import turtle as t
timm=t.Turtle()
colours=["red","brown","green","pink","black","orange","yellow","purple","blue","violet"]
def circle():
    for _ in range(36):
        timm.forward(15)
        timm.right(10)
for _ in range(36):
    timm.right(10)
    circle()
    timm.color(random.choice(colours))


    