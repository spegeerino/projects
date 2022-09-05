#answer: 694687
import functions as f
import numpy as np
def within_triangle0xy(x,y):
    #points such that x0 > 0, y0 > 0 and under the line from (x,0) to (0,y)
    #this line is y0 = (-y/x)x0 + y ==> xy0 + yx0 = xy, so we want xy0 + yx0 < xy
    #picks theorem: A = xy/2 = #interior points + #boundary points/2 - 1
    #num boundary points is just x+y-1 for left and bottom leg and then + points on the line xi + yj = xy
    #solutions to this for i and j are (0,x), (y,0), and there are gcd(x,y) - 1 more solutions i think
    #like assume x,y are rel prime then we have xi + yj = xy only for (0,x), (y,0) in nonneg integers
    #then if x,y are not rel prime then let d = gcd(x,y) and let h,k = x/d, y/d so we have
    # hi + kj = dhk has solutions for when (i,j) = (nk, (d-n)h) for all nonneg n and d-n, giving a total of 
    # d + 1 solutions
    out = x*y - x - y - np.gcd(x,y) + 2
    return out >> 1

def within_quadabcd(a,b,c,d):
    total = a+b+c+d-3
    total += within_triangle0xy(a,b)
    total += within_triangle0xy(a,d)
    total += within_triangle0xy(c,b)
    total += within_triangle0xy(c,d)
    return total

def withinallquads(m):
    count = 0
    for a in range(1,m+1):
        for b in range(1,m+1):
            for c in range(1,m+1):
                for d in range(1,m+1):
                    if f.is_square(within_quadabcd(a,b,c,d)):
                        count += 1
        print(str(a) + "%")
    return count

print(withinallquads(100))