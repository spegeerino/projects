from functions import gcd
count = 0
for denom in range(4, 12001):
    for numer in range(denom//3 + 1, denom//2 + 1):
        if gcd(numer,denom) == 1:
            count += 1
print(count)