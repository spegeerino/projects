# memoize
from functions import totient, is_prime
limit = 4 * 10**7
with open("primes.txt", "r") as primes_file:
    global primes
    primes = []
    s = primes_file.readline()
    while s and ((len(primes) == 0) or primes[-1] < limit):
        x = int(s)
        primes.append(x)
        s = primes_file.readline()
    primes.pop(-1)

count = 0
total = 0
vals = [-1] * (primes[-1] + 1)
vals[1] = 1
for i in range(2, len(vals)):
    vals[i] = 1 + vals[totient(i)]
    if i % 40000 == 0:
        print(i, count, total)
    if vals[i] == 25 and is_prime(i):
        count += 1
        total += i
print(count)
print(total)