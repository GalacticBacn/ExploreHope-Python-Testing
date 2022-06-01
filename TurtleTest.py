import turtle

turtle1 = turtle.Turtle()
turtle2 = turtle.Turtle()

# turtle1.pencolor("green")
# turtle2.pencolor("yellow")

window = turtle.Screen()

turtle1.shape("turtle")
turtle2.shape("turtle")

turtle1.color("yellow","green")
turtle2.color("red")
turtle1.begin_fill()
# turtle.dot()

window.bgcolor("blue")

while True:
    turtle1.forward(100)
    turtle1.right(50)
    turtle1.forward(10)
    
    turtle2.forward(100)
    turtle2.left(50)
    turtle2.backward(10)
    if abs(turtle1.pos()) < 1:
        break


# for i in [0,1,2,3]:
#     turtle1.forward(100)
#     turtle1.right(50)
#     turtle1.forward(10)
#     
#     turtle2.forward(100)
#     turtle2.left(50)
#     turtle2.backward(10)
    
turtle1.end_fill()