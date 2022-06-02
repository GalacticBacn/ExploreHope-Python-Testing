#from turtle import *
import turtle
import random

shapeList = ["arrow", "turtle", "circle", "square", "triangle", "classic"]
colorList = ["red", "green", "blue", "yellow"]

shapeRand = shapeList[random.randint(0,5)]
colorRand = colorList[random.randint(0,3)]

turtle.shape(shapeRand)

turtle.color(colorRand, colorRand)
turtle.begin_fill()

forwardRandInt = random.randint(50,200)
leftRandInt = random.randint(50,140)
backwardRandInt = random.randint(0,10)

index = 0

turtle.speed(0)
while True:
    turtle.forward(forwardRandInt)
    turtle.left(leftRandInt)
    turtle.backward(backwardRandInt)
    #turtle.backward(5)
    index=index+1
    if abs(turtle.pos()) < 1:
        break
    #elif (index>100):
        #break
turtle.end_fill()