#markov chain
#only thing that matters is how many 0s are left
#if no zeroes left: finished
#if one zero left, you have 1/2 chance to move to no zeroes left and 1/2 chance to move to one zero left.
#a1 = 1 + (a0/2 + a1/2) ==> a1 = 2
#a2 = 1 + (a0/4 + 2a1/4 + a2/4) ==> 3a2 = 4 + 0 + 2(2) = 8 ==> a2 = 8/3

import functions as f
from functools import cache
@cache
def a(n):
    if n == 0:
        return 0
    out = 1 << n #for the extra step
    for i in range(n):
        out += f.nchooser(n,i) * a(i) #skipping division by 2^n
    out /= (1 << n) - 1 
    return out

print(a(32)) 
