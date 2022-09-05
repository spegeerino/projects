from math import prod
from numpy import sort
import functions as f
from timeit import default_timer as dt
from functions import print_time_taken as ptt 
nums = set()
new_nums = set([1])
primes = f.prime_list(50)
limit = 10**13
print(prod(primes))
total = 0
start = dt()
while len(new_nums) != 0:
    nums = nums | new_nums
    temp = set()
    for p in primes:
        for x in new_nums:
            el = p*x
            if el < limit:
                temp.add(el)
    new_nums = temp
print("done generating")
ptt(start, dt())
sorted = sort(list(nums))
works = 0 
for i in range(len(sorted) - 1):
    if sorted[i+1] == sorted[i] + 1:
        total += sorted[i]
        works += 1
print(total)
print(works)
ptt(start, dt())