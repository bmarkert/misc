import turtle
import time

def draw_BM():
        window = turtle.Screen()
        window.bgcolor("violet")
        
        tortie = turtle.Turtle()
        tortie.shape("turtle")
        tortie.color("black")
        tortie.speed(3)
        
        time.sleep(2)
        
        tortie.circle(30, 180) # start writing 'B'
        tortie.left(90)
        tortie.forward(120)
        tortie.left(90)
        tortie.circle(30, 180)

        tortie.penup()

        tortie.setx(60)
        tortie.sety(-60)

        tortie.pendown()

        tortie.right(90) # start writing 'M'
        tortie.forward(120)
        tortie.right(150)
        tortie.forward(60)
        tortie.left(120)
        tortie.forward(60)
        tortie.right(150)
        tortie.forward(120)

        window.exitonclick()

draw_BM()
