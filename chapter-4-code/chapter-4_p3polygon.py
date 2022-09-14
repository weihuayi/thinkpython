import turtle

def polygon(t,length,n):
    '''
    t:一个Turtle对象
    length:多边形各边的长度，单位为像素
    n:多边形的边数
    该函数使用turtle模块来画出一个正多边形
    '''
    print(t)
    c = 360/n
    for i in range(n):
        t.fd(length)
        t.lt(c)
    

bob = turtle.Turtle()
polygon(bob,100,6)

turtle.mainloop()
