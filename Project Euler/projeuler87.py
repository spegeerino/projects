import math as m
import functions as f

limit = 50000000
sum_set = set()
primes = f.prime_list((int)(m.sqrt(limit)) + 1)

for p in primes:
    if p % 200 == 1:
        print(p)
    if p*p + 24 >= limit:
        break
    for q in primes:
        if p*p + q**3 + 16 >= limit:
            break
        for r in primes:
            r2 = r*r
            x = p*p + (q**3) + r2*r2
            if x >= limit:
                break
            else:
                sum_set.add(x)

print(len(sum_set))
