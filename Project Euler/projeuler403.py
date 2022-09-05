#lattice points between ax + b and x^2 for all integers (a,b) such that the area of R is rational
#and |a|, |b| < N = 10 ** 12
#x = (a +- sqrt(a^2 + 4b))/2, a^2 + 4b is pos
#b ranges from -a^2/4 to N
import math as ma
def D(a,b):
    x1 = ma.ceil((a - ma.sqrt(a*a + 4*b))/2)
    x2 = int((a + ma.sqrt(a*a +4*b))/2) + 1
    count = 0
    for x in range(x1, x2):
        count += a*x + b - x*x + 1
    return count


print(D(1,2))
