import turtle
#import math

#t = turtle.Turtle()

def polygon(t, n, length):
    angle = 360 / n
    for i in range(n):
        t.fd(length)
        t.lt(angle)
#print(t)

if __name__ == '__main__':

    bob = turtle.Turtle()
    polygon(bob, 39, 50)

    turtle.mainloop()
