# For an integer n ≥ 4, we define the lower prime square root of n, denoted by lps(n), 
# as the largest prime ≤ √n and the upper prime square root of n, ups(n), as the smallest prime ≥ √n.

# So, for example, lps(4) = 2 = ups(4), lps(1000) = 31, ups(1000) = 37.
# Let us call an integer n ≥ 4 semidivisible, if one of lps(n) and ups(n) divides n, but not both.

# The sum of the semidivisible numbers not exceeding 15 is 30, the numbers are 8, 10 and 12.
# 15 is not semidivisible because it is a multiple of both lps(15) = 3 and ups(15) = 5.
# As a further example, the sum of the 92 semidivisible numbers up to 1000 is 34825.

# What is the sum of all semidivisible numbers not exceeding 999966663333 ?
# ANSWER:
# ______________________________________________________________________________
import functions as f
from math import isqrt, floor
from timeit import default_timer as dt
upper = 999966663333
start = dt()
primes = f.prime_list(isqrt(upper) + 1)
primes.append(f.next_prime(primes))
count = 0
sum = 0
for i in range(len(primes) - 1):
    lp = primes[i]
    up = primes[i+1] 
    lb = lp*lp
    ub = min(up*up - 1, upper + 1)
    muls_of_lp = (ub // lp) - (lb // lp)
    muls_of_up = (ub // up) - (lb // up)
    sum_muls_lp = ((ub // lp) * muls_of_lp - (muls_of_lp * (muls_of_lp - 1))//2) * lp
    sum_muls_up = ((ub // up) * muls_of_up - (muls_of_up * (muls_of_up - 1))//2) * up
    sum += sum_muls_lp + sum_muls_up - 2 * lp * up
    count += muls_of_lp + muls_of_up - 2 #one multiple of both
    if upper + 1 < lp * up:
        count += 2
        sum += 2 * lp * up
print(count)
print(sum)
end = dt()
f.print_time_taken(start, end)