import turtle

'''
Created by DEDMURDERER
'''

screen = turtle.Screen()

drawer = turtle.Turtle()
drawer.speed('fastest')
drawer.penup()
drawer.hideturtle()
drawer.goto(drawer.xcor(), -50)
drawer.pendown()
drawer.begin_fill()


drawer.forward(800)
drawer.right(90)
drawer.forward(350)
drawer.right(90)
drawer.forward(1600)
drawer.right(90)
drawer.forward(350)
drawer.right(90)
drawer.forward(800)

drawer.end_fill()

t = turtle.Turtle()
t.speed('fastest')
t.setheading(270)
t.penup()

h = turtle.Turtle()
h.speed('fastest')
h.penup()
h.goto(t.pos())
h.right(90)
h.hideturtle()

g = 0.1
c = 0

def gravity():
    global c, g
    while t.ycor() > -50:
        t.goto(t.xcor(), t.ycor()-c*g)
        screen.update()
        print(f"c has a value of {c}")
        print(f"gravity set to {c*g}")
        c += 1
    
    c = 0



gravity()

def up():
    t.speed(1)
    y = 10
    
    if t.distance(h) < 5:
        while y > 0:
            t.goto(t.xcor(), t.ycor()+2*y)
            
        
            y -= 1
        
        y1 = 10
        for i in range(5):
            t.goto(t.xcor(), t.ycor()+y1/10)
            y1 += 2.5
    gravity()
    t.speed('fastest')
 
def left():
    x = 5
    while x > 0:
        t.goto(t.xcor()-x, t.ycor())
        h.goto(t.xcor(), -50)
        gravity()
        x -= 0.2
 
def right():
    x = 5
    while x > 0:
        t.goto(t.xcor()+x, t.ycor())
        h.goto(t.xcor(), -50)
        gravity()
        x -= 0.2

turtle.listen()
turtle.onkey(up, 'w')
turtle.onkey(left, 'a')
turtle.onkey(right, 'd')




screen.mainloop()
