from functools import cache
import functions as f
import timeit 
import math
import doctest
from random import random 
N = 10 ** 7
count = 0
fail_num = 0
for _ in range(N):
    count += 1
    x = 0
    y = random()
    while y > x:
        x = y
        y = random()
        count += 1
    fail_num += x
print(f"avg count: {count/N}")
print(f"avg last num: {fail_num/N}") 
    

