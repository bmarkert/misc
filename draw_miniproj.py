import turtle

def draw_square(some_turtle):

        for i in range(1,5):
                some_turtle.forward(200)
                some_turtle.right(90)

def draw_BM():
        window = turtle.Screen()
        window.bgcolor("violet")
        
        tortie = turtle.Turtle()
        tortie.shape("turtle")
        tortie.color("black")
        tortie.speed(3)
        tortie.turtlesize(3)
        
        tortie.circle(50, 180)
        tortie.left(90)
        tortie.forward(200)
        tortie.left(90)
        tortie.circle(50, 180)

        tortie.penup()

        tortie.setx(100)
        tortie.sety(-100)

        tortie.pendown()

        tortie.right(90)
        tortie.forward(200)
        tortie.right(150)
        tortie.forward(100)
        tortie.left(120)
        tortie.forward(100)
        tortie.right(150)
        tortie.forward(200)

        

        #for i in range(1,37):
                #draw_square(tortie)
                #tortie.right(10)

        #rocky = turtle.Turtle()
        #rocky.shape("arrow")
        #rocky.color("green")
        #rocky.circle(100)

        window.exitonclick()

draw_BM()
