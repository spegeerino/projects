from numpy import log10 
from functions import print_time_taken as ptt
from timeit import default_timer as dt
seek = 123
num = 678910
lb = log10(seek) % 1
ub = log10(seek+1) % 1
count = 0
upper = 2 * 10**8
timecheck = upper // 100
val = log10(2)
s = dt()
for i in range(upper):
    if i % timecheck == 0:
        print(i, count)
    checksum = (i*val) % 1
    if lb <= checksum and checksum < ub:
        count += 1
    if count == num:
        print(i)
        break  
if count < num:
    print('not found')
ptt(s, dt())