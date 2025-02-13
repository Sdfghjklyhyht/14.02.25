from turtle import *
screensize(1000,1000)
tracer(30)
pen(3)
lt(90)
n=10
down()
for i in range(10):
    for j in range(3):
        fd(10*n)
        rt(90)
        fd(10*n)
        rt(270)
    rt(90)
up()
for x in range(-100,100):
    for y in range(-100, 100):
        goto(x*n, y*n)
        dot(5, 'red')
done()
