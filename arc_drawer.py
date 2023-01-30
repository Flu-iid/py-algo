"""
this module will draw arc according to specific angle using degree or radiant
(degree as default) and preview by turtle module
"""
import turtle
import math

bob = turtle.Turtle()

# polygonal here

def polygon(side, length):
    outer_angle = 360 / side
    print(outer_angle)
    for i in range(side):
        bob.fd(length)
        bob.lt(outer_angle)


# circle here

def circle(radius):
    side_estimation = 360
    side = int(-1 / (radius - (side_estimation-4)/(side_estimation-3)) + side_estimation)
    length = (2*math.pi*radius)/side
    polygon(side, length)

circle(5)

#arc here



if __name__ == "__main__":
    print(bob)
    turtle.mainloop()
