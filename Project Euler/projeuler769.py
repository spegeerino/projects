#f(x,y) = x^2 + 5xy + 3y^2 = (x+sqrt(3)y)^2 + (5-2sqrt(3))xy
#
#f(x,y) = (x + 5y/2)^2 - 13y^2/4 = (x + (5+sqrt(13)/2)y) (x+(5-sqrt(13)/2)y)
#does this turn into pells?
#it's pells with annoying sqrt(13) attached and dyadic rationals
# a = 5/2, b = sqrt(13)/2, a^2 + 2ab + b^2 = 25/4 + 13/4 + 5sqrt(13)/2 
# (x0 + (a+b)y0)(x + (a+b)y)(x0 + (a-b)y0)(x + (a-b)y)
# ((x0x + (a+b)^2 * y0y) + (xy0+x0y)(a+b))((x0x + (a-b)^2 * y0y))
# x_new = (x0x + 3y0y), y_new = xy0 + x0y
# (x0 + (a+b)y0)(x + (a+b)y)(x0 + (a-b)y0)(x + (a-b)y)
#let y = x+c
#x^2 + 5x^2 + 5cx + 3x^2 + 6cx + 3c^2 = z^2 --> 9x^2 + 11cx + 3c^2 = z^2 
#c^2 + 11cx/3 + 3x^2
import functions as funcs
import numpy as np
def f(x,y):
    return x*x + 5*x*y + 3*y*y
def c(z):
    out = 0
    z2 = z*z
    for x in range(1,z):
        for y in range(1,z):
            if np.gcd(x,y) != 1:
                continue
            func = f(x,y)
            if func > z2:
                break
            if func == z2:
                print((x,y,z))
                out += 1
                break
    return out
print(c(87))
def C(N):
    out = 0
    for i in range(3,N,2):
        out += c(i)
        if i % 20 == 1:
            print(out/i)
    return out
print(C(10001))