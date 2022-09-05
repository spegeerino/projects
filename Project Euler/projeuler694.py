#ANSWER: 
# A positive integer n is considered cube-full, if for every prime p that divides n, so does p^3.
# Note that 1 is considered cube-full.
# Let s(n) be the function that counts the number of cube-full divisors of n. 
# For example, 1, 8 and 16  are the three cube-full divisors of 16. 
# Therefore, s(16) = 3.
# Let S(n) represent the summatory function of s(n), that is S(n) = sum from i=1 to n of s(i)
# You are given S(16) = 19, S(100) = 126, S(10000) = 13344

# Compute S(10^18).
import functions as f
import numpy as np
limit = 10 ** 6
biglimit = 10 ** 18
primes = f.prime_list_sieve(limit)
