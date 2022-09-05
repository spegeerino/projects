#strong repunits
#N is a repunit in base b iff it can be written as (b^x - 1 / b - 1)
#N is always a repunit in base N-1, so we only need to check b^2 + b + 1, b^3 + b^2 + b + 1, and so on
from math import isqrt
vals = set()
limit = 10 ** 12
upper = isqrt(limit) 
for b in range(2, upper + 1):
    if b % 1000 == 0:
        print(b)
    exp = 3
    num = b*b + b + 1
    while num < limit:
        vals.add(num)
        num += b ** exp 
        exp += 1
print(sum(vals) + 1)
