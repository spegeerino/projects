from timeit import default_timer as dt
from functions import print_time_taken as ptt 
def check(n):
    for splt in all_splits(n*n, n*n):
        if sum(splt) == n:
            return 1
    return 0

def all_splits(n, orig_n = 0):
    if n < 10:
        return [[n]]
    excl_last = all_splits(n//10, orig_n)
    out = []
    last = n % 10
    for lst in excl_last:
        concat = list(lst)
        concat[-1] = concat[-1] * 10 + last 
        if concat[-1] <= orig_n:
            out.append(concat)
        addit = list(lst)
        addit.append(last)
        out.append(addit)
    return out 

s = dt()
total = 0
limit = 10 ** 6
for i in range(10, limit + 1, 9):
    if i % (limit // 100) == 0:
        print(i)
    if check(i-1):
        total += (i-1)*(i-1)
        # print(i-1, (i-1)*(i-1))
    if check(i):
        total += i*i
        # print(i, i*i)
print(total)
ptt(s, dt())