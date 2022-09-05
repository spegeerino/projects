#sum of first 40 prime factors of R(10^9)
#R(k) = (10^k - 1)/9
#assume k not multiple of 3, we know R(k) ends in 1 and thus not mul of 2 or 5
import functions as f
primes = [2,3,5,7]
num_primes = 40
expo = 10**9
vals = []
while len(vals) < num_primes:
    p = primes[-1]
    checksum = pow(10, expo % (p-1), p)
    checksum = ((checksum + p - 1) * f.mod_inverse(9, p)) % p 
    if checksum == 0:
        vals.append(p)
    primes.append(f.next_prime(primes))
print(vals)
print(sum(vals))