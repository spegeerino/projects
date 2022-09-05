#ANSWER: 11109800204052
# The largest integer ≤ 100 that is only divisible by both the primes 2 and 3 is 96, 
# as 96=32*3=2^5*3. For two distinct primes p and q 
# let M(p,q,N) be the largest positive integer ≤N only divisible by both p and q 
# and M(p,q,N)=0 if such a positive integer does not exist.

# E.g. M(2,3,100)=96.
# M(3,5,100)=75 and not 90 because 90 is divisible by 2 ,3 and 5.
# Also M(2,73,100)=0 because there does not exist a positive integer ≤ 100 that is divisible by both 2 and 73.

# Let S(N) be the sum of all distinct M(p,q,N). S(100)=2262.

# Find S(10 000 000).

# tentative guess: 11109800204052, code is prob broken as always nope it was right
# also learned pow(base, exp, mod) gives base^exp mod mod
# i should use this more because it's so fast because C strong

#S(100): (2,3,96), (2,5,100), (2,7,98), (2,11,88), (2,13,52), (2,17,68), (2,19,76), (2,23,92)...
import functions as f
import numpy as np
total = 0
limit = 10 ** 7
loglimit = np.log10(limit)
firstfail = False
primes = f.prime_list_sieve(5000000)
print("primes calculated")
for i in range(len(primes)):
    if firstfail:
        break
    p = primes[i]
    print(p)
    for j in range(i+1, len(primes)):
        q = primes[j]
        lcm = p*q
        if lcm > limit: 
            if j == i+1:
                firstfail = True
            break
        maxpower = int((loglimit - np.log10(p))/np.log10(q))
        #if maxpower == 0:
         #   print((p,q,maxpower))
        # p^m*q^n <= limit
        # mlog10(p) + nlog10(q) <= log10(limit) = 2 or 7 depending
        # min m = 1, nlog10(q) <= 2 - log10(p)
        # n <= [2 - log10(p)] / log10(q) 
        maxguess = lcm
        for k in range(1,maxpower + 1):
            guess = p * q ** k
            while guess <= limit: 
                guess *= p
            guess //= p 
            if guess > maxguess:
                maxguess = guess
        #print((p,q,maxguess, maxpower))
        total += maxguess
print(total)
print("testing")
print(int((7 - np.log10(2))/np.log10(209189)))