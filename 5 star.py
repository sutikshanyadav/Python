# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import turtle
t=turtle.Turtle()
t.speed(100)

screen = turtle.Screen()
screen.bgcolor("black")
star_turtle = turtle.Turtle()
star_turtle.color("blue")
star_turtle.speed(5)

# Function to draw a star
def draw_star(size):
    for _ in range(5):
        star_turtle.forward(size)
        star_turtle.right(144)

# Draw the star
draw_star(100)

# Hide the turtle

star_turtle.penup()
star_turtle.goto(-50, 0)
star_turtle.pendown()
star_turtle.hideturtle()
screen.mainloop()

        






 
