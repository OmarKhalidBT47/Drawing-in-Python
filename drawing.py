from shapes import *


turtle.screensize(X_MAX, Y_MAX)
# drawing a block
turtle.penup()
turtle.goto(X_MIN, Y_MIN)
turtle.pendown()

for i in range(4):
    turtle.forward(X_MAX * 2)
    turtle.left(90)

draw_shape("r", "red", 0, 0, 50, 50)
draw_shape("c", "green", 50, 60, 60)
draw_shape("t", "blue", -100, 50, 70)
turtle.mainloop()