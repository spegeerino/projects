# the complex thing
# gcd(m,n) = 1, m+n is odd 
# m^2 + n^2 < N
#
from math import isqrt
from re import S 
from numpy import gcd 
from timeit import default_timer as dt
from functions import print_time_taken as ptt 
from functions import totient
import functions as f
limit = 3141592653589793
def naive_sol(N):
    upper = isqrt(N)
    timecheck = upper // 1000
    count = 0
    start = dt()
    for m in range(2,upper + 1):
        if m % timecheck == 0:
            print(m)
        for n in range(1 + (m%2), m, 2):
            if m*m + n*n > N:
                break
            count += (gcd(m,n) == 1)
    print(count)
    ptt(start, dt())

def sol(N):
    upper = isqrt(N)
    timecheck = upper // 100
    count = 0
    start = dt()
    for m in range(2, upper + 1):
        if m % timecheck == 0:
            print(m)
        if m % 2 == 0:
            count += totient(m)
        else:
            count += totient(m) // 2
    print(count)
    ptt(start, dt())

def even_totient(n):
    x = f.pf(n)
    for k in x.keys():
        pass
    return n

sol(limit)