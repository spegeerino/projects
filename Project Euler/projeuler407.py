import functions as f
import math as m

def crt(primes, mods):
    starter = 0
    arith_prog = 1
    for i in range(len(primes)):
        p = primes[i] 
        for j in range(p):
            x = starter + arith_prog * j
            if x % p == mods[i]:
                starter = x
                break
        arith_prog *= p
    return starter

def better_crt(primes,mods):
    product = 1
    for p in primes:
        product *= p
    y_list = []
    for p in primes:
        y_list.append(product//p)

def max_idempotent(n):
    n_pf = f.pf(n)
    max = 0
    for i in range(1 << len(n_pf.keys())):
        mods = [int(x) for x in str(bin(i))[2:]]
        while len(mods) < len(n_pf.keys()):
            mods.insert(0,0)
        new = crt(list(n_pf.keys())[::-1],mods)
        if new > max:
            max = new
    return max
timecheck = 10**4
def main():
    total = 0
    for i in range(2, 10**7 + 1):
        if i % timecheck == 0:
            print(i)
        total += max_idempotent(i)
    print(total)

if __name__ == "__main__":
    main()