import numpy as np
import timeit
limit = 3001

def length_of_recurring_cycle(denom):
    residues = [1]
    for i in range(denom-1):
        x = residues[-1] * 10 
        x %= denom
        if x == 0:
            return 0
        for j in range(len(residues)):
            if x == residues[j]:
                return i - j + 1
        residues.append(x)
    return denom - 1

def elim_factors_of_two_and_five(x):
    while x & 1 == 0:
        x = x // 2
    while x % 5 == 0:
        x = x // 5
    return x

def has_two_or_five(n):
    return ((n & 1) == 0) or (n%5 == 0)

sum = 0

sum2 = 0
a_s = timeit.default_timer()
for i in range(3, limit):
    if i % 1000 == 0:
        print(i)
    if not has_two_or_five(i):
        n = length_of_recurring_cycle(i)
        val = limit//i
        scalar = 0
        two_max = int(np.log2(val)) + 1
        for i in range(two_max):
            five_max = np.log2(val) // np.log2(5)
            scalar += five_max + 1
            val = val / 2
        sum += scalar * n
a_e = timeit.default_timer()
b_s = timeit.default_timer()
for i in range(3, limit):
    sum2 += length_of_recurring_cycle(i)
b_e = timeit.default_timer()
print(sum)
print(a_e-a_s)
print(sum2)
print(b_e - b_s)