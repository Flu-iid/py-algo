import turtle
import math

bob=turtle.Turtle()

def square(t, length):
 for i in range(4):
  t.fd(length)
  t.lt(90)

def polygen(t, length, n):
 for i in range(n):
  t.fd(length)
  t.lt(360/n)

def circle(t, r):
 n=360
 length=2*math.pi*r/n
 polygen(t, length, n)

def arc(t, r, angle):
  n=360
  length=2*math.pi*r/n
  for i in range(angle):
    t.fd(length)
    t.lt(360/n)

def flower(t, r, angle, f):
  n=360
  length=2*math.pi*r/n
  for i in range(angle):
    t.pd()
    t.fd(length)
    t.lt(360/n)
  for i in range(180):
    t.pu()
    t.fd(length)
    t.lt(360/n)
  for i in range(angle):
    t.pd()
    t.fd(length)
    t.lt(360/n)
  
  t.pu()
  t.rt(360/f)
  
  for i in range(angle):
    t.pd()
    t.fd(length)
    t.lt(360/n)
  for i in range(180):
    t.pu()
    t.fd(length)
    t.lt(360/n)
  for i in range(angle):
    t.pd()
    t.fd(length)
    t.lt(360/n)
  
  t.pu()
  t.rt(360/f)

  for i in range(angle):
    t.pd()
    t.fd(length)
    t.lt(360/n)
  for i in range(180):
    t.pu()
    t.fd(length)
    t.lt(360/n)
  for i in range(angle):
    t.pd()
    t.fd(length)
    t.lt(360/n)
  
  t.pu()
  t.rt(360/f)

  for i in range(angle):
    t.pd()
    t.fd(length)
    t.lt(360/n)
  for i in range(180):
    t.pu()
    t.fd(length)
    t.lt(360/n)
  for i in range(angle):
    t.pd()
    t.fd(length)
    t.lt(360/n)
  
  t.pu()
  t.rt(360/f)



def circle2(t, r):
  circumference=2*math.pi*r
  n=int(circumference/3)+1
  length=circumference/n
  polygen(t, length, n)



    
print(circle2(bob, 1))

turtle.mainloop()