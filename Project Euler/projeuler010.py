from math import isqrt
from functions import prime_list
#there is an absolutely beautiful algorithm in the thread for this problem which i want to code here
#we don't have to compute all the primes < 2*10^6 to find their sum
#we do this via dynamic programming
#Let V(n, p) be the sum of all integers from 2 to n (not including n) that remain after sieving with all numbers less than or equal to p.
#note we choose 2 to n to avoid problems with 1's primality
#then, consider what V(n,p) is in terms of V(n, p-1).
#if p isn't prime, then sieving with it doesn't remove anything (since primes already sieved out its multiples),
# so in that case V(n, p) = V(n,p-1)
#if p is prime, then we remove multiples of p which have no smaller factor than p that are still left in the list of numbers
# so we should have V(n, p) = V(n, p-1) - (something)
# how do we determine what to subtract? 
# well, we can subtract out all the multiples of p times any number in the sieve, 
# and then add back p times any primes less than p, since we will have already sieved those out prior to sieving by p
# we can easily find those by looking at V(p,p), which is just all the primes less than p (after sieving out by all nums in the range, only primes will be left)
# that looks like V(n, p) = V(n,p-1) - p[V(n//p, p-1) - V(p-1,p-1)]
# so we have a formula for both cases, now we implement
# the goal is to get to V(2*10^6, k) with k > sqrt(2*10^6), as then we'll have sieved out by all primes > the sqrt of the limit
# which removes all composites. 
# since all V(n, p) only depend on info of the form V(x, p-1)
# we can iterate over all p
# then since V(n,p) only depends on info of the form V(x, p-1) with x <= n, we can iterate top down on the ns
# implemented below

def sol(x):
    max_k = isqrt(x)
    ns_arr = [x//k for k in range(1, max_k + 1)] 
    ns_arr += list(range(ns_arr[-1] - 1, 0, -1)) #all nums of the form n // k that are positive integers (in top down order)
    dp = {i:i*(i+1)//2 - 1 for i in ns_arr} #S(n, 1) for all n in ns_arr
    for p in range(2, max_k + 1):
        if dp[p] > dp[p-1]: #p is prime, essentially asking if S(p, p-1) > S(p-1, p-1); if p not prime then p gets sieved out and sums are equal 
            sum_primes_less_p = dp[p-1] #S(p-1, p-1)
            p_sqr = p*p 
            for n in ns_arr:
                if n < p_sqr: #if n < p_sqr, no sieving to be done (no multiples of p that haven't already been sieved) so we quit out
                    break
                dp[n] -= p*(dp[n//p] - sum_primes_less_p) 
    return dp[x]

print(sol(2 * 10 ** 6))


