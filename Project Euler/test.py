from functools import cache
import functions as f
import timeit 
import math
import doctest
from random import random, randint
N = 10 ** 3
count = 0
def max_greater_than(n):
    for i in range(12):
        if n < i*i*i:
            return i-1

for i in range(1, N+1):
    x = max_greater_than(i)
    if i % x == 0:
        count += 1
print(count * 5, N - count)

successes = 0
fails = 0
trials = 10 ** 7
for _ in range(trials):
    a = randint(1, 1000)
    b = max_greater_than(a)
    if a % b:
        fails += 1
    else:
        successes += 1

print((5*successes - fails)/trials)