from functions import reverse, prime_list
from functions import gen_prime_sieve as gps
from timeit import default_timer as dt
# with open("primes.txt","r") as primes_file:
#     global primes
#     primes = []
#     curr = primes_file.readline()
#     while curr:
#         primes.append((int)(curr))
#         curr = primes_file.readline()

primes = gps(10**8)
print("primes are loaded")

data = {}
total = 0
count = 0
for p in primes:
    p2 = p*p
    p2r = reverse(p2)
    if p2r in data:
        total += p2 + p2r
        count += 2
    data[p2] = 1
    if count == 50:
        break
print(total, count)

