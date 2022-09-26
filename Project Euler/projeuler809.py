from functools import cache
from numpy import gcd

data = {}
def naive(a,b):
    if b == 2:
        return a//b + 2
    if (a,b) in data:
        return data[(a,b)]
    d = gcd(a,b)
    a //= d
    b //= d
    if a % b == 0:
        out = a // b
        data[(a,b)] = out
        return a // b
    if a < b:
        out = naive(b, b-a)
        data[(a,b)] = out
        return out
    # denom of first expression is c / b
    c = (-a) % b
    # (b - c)/c
    out = naive(b-c + c*naive(a-b, b), c)
    data[(a,b)] = out
    return out

# suppose we take f(1/6) --> f(6/5) --> f(1 + 4f(1/5)/4) --> f(1/5) needs to be calc'd
# f(nk + 1, n) = f(n - (n-1) + (n-1)f(n(k-1)+1, n), n-1) = f(1 + (n-1)f(n(k-1)+1, n), n-1)
# f(1 + (n-1)f(1 + (n-1)f(n(k-2) + 1,n), n-1), n-1) continue until k depletes to 0
# what do i need to pre calculate: 
def naivef(n, k):
    return naive(n*k+1, n)

for n in range(3, 6):
    print(n)
    for k in range(1, 3**(13-n*n//2)):
        x = naivef(n,k)
        print(f"naive({n * k + 1}, {n}) = {x}")
    print("-" * 40)