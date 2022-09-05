# nums that can be written as (2a+1)^2 - (2b+1)^2 or (2a)^2 - (2b)^2
# N = x^2 - y^2 = (x-y)(x+y), how many factor pairs of N are there, x > y > 0 and are integers
# this requires factor pair to have both evens or both odds
# chances of this are |(x-1)/x+1| where x is the exponent of 2 in the pf of n
#basically if N is square it's # factors - 1 / 2, otherwise it's just #factors/2
#prime factorization is already nsqrt(n) though, right too slow
#well not necessarily
#if they have at least 11 factor pairs they must have at least 22 factors 
# which means at least 5 not necessarily unique prime factors, which makes prime factorization faster kind of
import functions as f
limit = 10**6
count = 0
for i in range(2, limit + 1, 2):
    if i % 10000 == 0:
        print(i)
    numpf = f.pf(i)
    val = f.pf_num_of_divisors(numpf) 
    if 2 in numpf.keys():
        val //= numpf[2] + 1
        val *= numpf[2] - 1
    if 1 < val and val <= 21:
        # print(i)
        # print(numpf)
        count += 1
print(count)
