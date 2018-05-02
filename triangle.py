from turtle import *

color('black', 'green')
penup()
setpos(-150, -100)
pendown()

def build(width, n):
    if n > 0:
        build(width/2, n-1)
        forward(width/2)
        build(width/2, n-1)
        left(60)
        forward(width/2)
        left(60)
        build(width/2, n-1)
        right(120)
        backward(width/2)
        left(60)
        backward(width/2)
        right(60)
        
    else:
        begin_fill()
        for i in range(3):
            forward(width)
            left(120)
        end_fill()

    
build(300,3)

done()