import turtle
from math import pi

def polygon(t,length,n): 
    print(t)
    c = 360/n
    for i in range(n):
        t.fd(length)
        t.lt(c)

def circle(t,r,angle=360):
    '''
    t:一个turtle对象
    r:圆的半径
    angle:画出圆弧的角度，默认为360度，即画出一个圆
    该函数使用turtle模块来画出一个圆
    '''
    print(t)
    c = 2*pi*r
    n=100
    a = 360/n
    length = c/n
    n = int(n*(angle/360))
    for i in range(n):
        t.fd(length)
        t.lt(a)

bob = turtle.Turtle()
circle(bob,100,angle=270)
turtle.mainloop()

