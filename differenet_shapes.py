import random
import turtle as t
timm=t.Turtle()
colours=["red","brown","green","pink","black","orange","yellow","purple","blue","violet"]
def draw_shape(num_sides):
    angle=360/num_sides
    for _ in range(num_sides):
        timm.forward(100)
        timm.right(angle)
for shape_side_n in range(3,11):
    timm.color(random.choice(colours))
    draw_shape(shape_side_n)
