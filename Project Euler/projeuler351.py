#ANSWER: unknown
import functions as f
import numpy as np
def H(n):
    #one line has n-1 hidden points
    out = n-1
    for i in range(2,n+1):
        if i % 100000 == 0:
            print(i)
        numer = 1
        denom = 1
        for p in f.pf(i).keys():
            numer *= p-1
            denom *= p
        out += i * numer // denom
    return out * 6
    #this sum has to be reducible somehow
limit = 10 ** 8
print(H(5))
print(H(10))
print(H(1000))
