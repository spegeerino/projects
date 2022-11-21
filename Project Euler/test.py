from functools import cache
import functions as f
import timeit 
import math
import doctest
from random import random, randint
nvals = {}
for n in range(1, 5000):
    if n % 100 == 0:
        print(n)
    tup = [1,1,1,1,0]
    count = 0
    while tup[0] <= math.pow(n, 0.2):
        tup[-1] += 1
        if math.prod(tup) > n:
            i = -2
            while math.prod(tup) > n and i >= -len(tup):
                tup[i] += 1
                for j in range(i + 1, 0):
                    tup[j] = tup[i]
                i -= 1
        if n % math.prod(tup) == 0:
            # print(tup)
            nums = {}
            for k in tup:
                if k in nums:
                    nums[k] += 1
                else:
                    nums[k] = 1
            toadd = 120
            for k in nums:
                toadd //= math.factorial(nums[k])
            count += toadd
    # print(count)
    x = count / n
    nvals[n] = x
nums = []
best = 0
for k in nvals:
    if nvals[k] > best:
        best = nvals[k]
        nums = []
        nums.append((k, nvals[k]))
    elif nvals[k] == best:
        nums.append((k, nvals[k]))
print(nums)
print(best)