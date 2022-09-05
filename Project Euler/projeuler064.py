import math
count = 0
limit = 10 ** 4
notsquares = []
for i in range(2,limit + 1):
    if not (int)(math.sqrt(i)) ** 2 == i:
        notsquares.append(i)

for n in notsquares:
    period = 0
    frac_n = set()
    maxremovable = (int)(math.sqrt(n))
    a = maxremovable
    numer2 = a
    denom = n - numer2 * numer2
    while period == len(frac_n):
        a = (numer2 + maxremovable) // denom 
        numer2 = denom * a - numer2
        denom = (n - numer2 * numer2) // denom
        frac_n.add((numer2,denom,a))
        period += 1
    if len(frac_n) % 2 == 1:
        count += 1
        print(n)

print(count)