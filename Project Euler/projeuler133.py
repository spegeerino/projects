# R(n) = (10^n - 1) / (10 - 1)
# R(10^n) = (10^(10^n) - 1) / (10 - 1)
# need (10^(10^n) - 1) = 0 mod p --> 10^(10^n) = 1 mod p
# FLT says 10^n = 0 mod p - 1 (EDIT: is a possible solution, but not guaranteed to find all sols)
# this only possible if 10^n is a multiple of p-1  
import functions as f
from timeit import default_timer as dt
from functions import print_time_taken as ptt 
limit = 10 ** 2
primes = f.prime_list(limit)
total = 0 
for p in primes[3:]:
    x = p-1
    while x % 2 == 0:
        x //= 2 
    while x % 5 == 0:
        x //= 5 
    if x != 1:
        total += p 
        print(f"{p} doesn't work")
        # sufficient but not necessary; period can be a factor of p-1 
    else:
        print(f"{p} works")
print(total)
