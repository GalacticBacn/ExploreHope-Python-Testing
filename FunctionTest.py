# Testing Functions with Turtles
import turtle
import random

bob = turtle.Turtle()
joe = turtle.Turtle()

bob.speed(1)
joe.speed(1)

def main():
    screen()
    
    bob.forward(100)
    joe.left(50)
    
    bob.right(90)
    joe.forward(50)
    
    bob.forward(100)
    joe.forward(20)
    
def screen():
    
    window = turtle.Screen()
    window.bgcolor("yellow")
    
main()