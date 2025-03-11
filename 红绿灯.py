from turtle import *
bgcolor("black")
delay(0)
ht()
up()
#color('greeen')
a = 'green', 'yellow', 'red'
x = 0
y = -300
pensize(20)
for cl in a:
    goto(x, y)
    color('white', cl)
    begin_fill()
    down()
    #for i in range(1, 10):
    circle(100, 360, steps=10)
    up()
    end_fill()
    y += 200
    
    #right(180)
#    forward(200)
#    left(170)
#    if abs(pos()) < 1:
#        break
done()
