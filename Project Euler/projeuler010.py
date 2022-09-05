#there is an absolutely beautiful algorithm in the thread for this problem which i want to code here
#we don't have to compute all the primes < 2*10^6 to find their sum
#we do this via dynamic programming
#Let V(n, p) be the sum of all integers from 2 to n (not including n) that remain after sieving with all numbers less than p.
#note we choose 2 to n to avoid problems with 1's primality
#then, consider what V(n, p+1) is.
#if p isn't prime, then sieving with it doesn't remove anything (since smaller primes already sieved out its multiples),
# so in that case V(n, p+1) = V(n,p)
#if p is prime, then we remove multiples of p which have no smaller factor than p that are still left in the list of numbers
# so we should have V(n, p+1) = V(n,p) - (something)
# how do we determine what to subtract? 
# well, we can subtract out all the multiples of p times any number in the sieve, 
# and then remove p times any primes less than p, since those will be the only exceptions
# we can easily find those by looking at V(p,p), which is just all the primes less than p (after sieving out by all nums in the range, only primes will be left)
# that looks like V(n, p+1) = V(n,p) - [pV(n//p, p) - pV(p,p)]
# so we have a formula for both cases, now we implement
# the goal is to get to V(2*10^6, k) with k > sqrt(2*10^6), as then we'll have sieved out by all primes > the sqrt of the limit
# which removes all composites. 
# 

def sol(n):

