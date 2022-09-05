import functions as f
from timeit import default_timer as dt
from numpy import log 
import math as m 
#500500 prime is about 7.5 mil
out = 1
limit = 75 * 10**5
desired = 500500
count = 0
valid = [1,2,4,8,16]
mod = 500500507
start = dt()
def custom_pf(n):
    if n == 1:
        return {}
    for i in range(2, (int)(m.sqrt(n) + 1)):
        if n % i == 0:
            p_index = 0
            newnum = n
            while newnum % i == 0:
                p_index += 1
                newnum //= i
            if newnum != 1:
                return
            return {i:p_index}
    return {n:1}

for i in range(2, limit):
    if i % 75000 == 0:
        print(i, count)
    i_pf = custom_pf(i)
    if i_pf and len(i_pf.keys()) == 1:
        if i_pf[list(i_pf.keys())[0]] in valid:
            out *= i
            out %= mod 
            count += 1
    if count == desired:
        print(i)
        break
print(out)
f.print_time_taken(start, dt())


