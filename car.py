import turtle
c=turtle.Turtle()
s=turtle.Screen()
c.speed(10)

d=100
r=40
a=90

c.forward(d)
c.right(a)

c.fillcolor("black")
c.begin_fill()
c.circle(r)
c.end_fill()

c.up()
c.goto(d+2*r,0)
c.down()

c.left(a)
c.forward(d-10)
c.left(a)
c.forward(d-r)
c.left(a)
c.forward(d-20)
c.right(a/2)
c.forward(d)
c.left(a/2)
c.forward(d*2)
c.left(a/2)
c.forward(d)
c.right(a/2)
c.forward(d-10)
c.left(a)
c.forward(d-r)
c.right(a)
c.forward(-d)
c.right(a)

c.fillcolor("black")
c.begin_fill()
c.circle(-r)
c.end_fill()

c.up()
c.goto(0,0)
c.down()

c.left(a)
c.forward((70*d)/100)

c.up()
c.goto(0,-10)
c.down()


c.hideturtle()
s.exitonclick()
