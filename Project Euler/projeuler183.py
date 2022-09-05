import numpy as np
from timeit import default_timer as dt 
from functions import print_time_taken as ptt 
import functions as f
from math import floor, ceil
total = 0
limit = 10000
s = dt()
for n in range(5, limit + 1):
    lt = floor(n/np.e)
    ut = ceil(n/np.e)
    lcs = lt*np.log(n/lt)
    ucs = ut*np.log(n/ut)
    denom = 0
    if ucs > lcs:
        denom = ut
    else:
        denom = lt
    denom = denom // np.gcd(n, denom)
    while denom % 2 == 0:
        denom //= 2
    while denom % 5 == 0:
        denom //= 5 
    if denom != 1:
        total += n
    else:
        total -= n 
print(total)
ptt(s, dt())
    