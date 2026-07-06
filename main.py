from turtle import *
t = Turtle()
t.color('blue')
t.pensize(5)
t.shape('circle')
t.speed(50)
def draw(x, y):
    t.goto(x, y)
def chto_to(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
def setblue():
    t.color('blue')
def setgreen():
    t.color('green')
def setred():
    t.color('red')
def startfill():
    t.begin_fill()
def endfill():
    t.end_fill()
def up():
    t.goto(t.xcor(), t.ycor()+5)
def left():
    t.goto(t.xcor()-5, t.ycor())
def down():
    t.goto(t.xcor(), t.ycor()-5)
def right():
    t.goto(t.xcor()+5, t.ycor())
scr = t.getscreen()
t.ondrag(draw)
scr.onscreenclick(chto_to)
scr.listen()
scr.onkey(setgreen, 'g')
scr.onkey(setred, 'r')
scr.onkey(setblue, 'b')
scr.onkey(startfill, 'f')
scr.onkey(endfill, 'e')
scr.onkey(up, 'w')
scr.onkey(left, 'a')
scr.onkey(down, 's')
scr.onkey(right, 'd')
