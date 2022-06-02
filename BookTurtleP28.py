import turtle

turtle1 = turtle.Turtle()
wn = turtle.Screen()

turtle1.pencolor("yellow")
wn.bgcolor("red")

def main():
#     for i in [0,1,2,3]:
#         turtle1.forward(150)
#         turtle1.left(90)
    for i in [0,1,2,3,4,5,6,7,8,9]:
        for i in [0,1,2,3]:
            turtle1.forward(150)
            turtle1.left(90)
        turtle1.right(36)
    
main()