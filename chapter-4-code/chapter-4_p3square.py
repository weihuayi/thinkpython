import turtle

def square(t,length):
    '''
    t:一个Turtle对象
    length:正方形的边长
    该函数使用turtle模块生成一个正方形
    '''
    print(t)
    for i in range(4):
        t.fd(length)
        t.lt(90)

bob = turtle.Turtle()
square(bob,200)
turtle.mainloop()


