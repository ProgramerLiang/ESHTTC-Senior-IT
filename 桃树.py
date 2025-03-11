from random import *
from turtle import *
#d = int(input("树干宽度为？\n"))
d = 30
def branch(depth):
    if depth <= 3:
        color('chartreuse')
        pensize(7)
        down()
        dot()
        fd(3)
        up()
        pensize(4)
        color('lightpink')
        fd(1)
        down()
        dot()
        up()
        bk(4)
    else:
        color('sienna')
        pensize(depth)
        length = depth * 5
        down()
        fd(length)
        up()
        totdeg = 0
        rt(75)
        while totdeg < 90:
            deg = randint(5,60)
            
            lt(deg)
            branch(depth - 5)
            totdeg += deg
        rt(totdeg-75)
        bk(length)
ht()
delay(0)
screensize(1024, 1024)
bgcolor('cornsilk')
up()
goto(0, -270)
color('sienna')
lt(90)
branch(d)
#pensize(d)
#down()
#goto(0, -270)
#up()
#branch(d - 5)
