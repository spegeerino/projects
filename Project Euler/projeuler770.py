import numpy as np
import functools
def E(g,t):
    if g == 0:
        return (1,1)
    if t == 0:
        return (1 << g,1)
    #E(g,t) = (1+x)E(g-1,t) = (1-x)E(g,t-1)
    #y = 1+x, 2-y = 1-x
    #y(E(g-1,t)+E(g,t-1)) = 2E(g,t-1)
    #y = 2E(g,t-1) / (E(g-1,t) + E(g,t-1))
    #E(g,t) = 2E(g,t-1)E(g-1,t) / (E(g-1,t) + E(g,t-1))
    a,b = E(g-1,t)
    c,d = E(g,t-1)
    numer,denom = 2*a*c, a*d + b*c
    divisor = np.gcd(numer,denom)
    numer //= divisor
    denom //= divisor
    return (numer,denom)
    #numer/denom = (2ac/bd) / ((ad+bc)/bd)
    #numer/denom = (2ac/(ad+bc))
print(E(4,4))

desirednumer = 17
desireddenom = 10
def compare_to_desired(a,b):
    if a*desireddenom >= b * desirednumer:
        return True
    return False

for i in range(11):
    a,b = E(i,i)
    print(i)
    print((a,b))
    print(compare_to_desired(a,b))