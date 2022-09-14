import turtle

bob = turtle.Turtle()
print(bob)

# 画一个正方形
'''
bob.fd(100)
bob.lt(90)
bob.fd(100)
bob.lt(90)
bob.fd(100)
bob.lt(90)
bob.fd(100)
'''

for i in range(4):
    bob.fd(100)
    bob.lt(90)

turtle.mainloop()

