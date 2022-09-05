import functions as f 
primes = f.prime_list(10**6)
for i in range(len(primes)):
    p = primes[i]
    x = pow(p-1, i+1, p*p) + pow(p+1, i+1, p*p)
    x %= p*p
    if x > 10 ** 10:
        print(i+1)
        print(p)
        break 