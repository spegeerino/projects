# sliding game
# ans:
# 2x num sols to 6a + 8b + 1 = p^2 for nonnegative a,b (a = n-m-1, b = m-1)
# identical to 3a + 4b = (p^2 - 1) / 2
import functions as f
from timeit import default_timer as dt
def numSols(n):
    out = n // 12
    if n % 12 <= 2 or n % 12 == 5:
        return out
    return out + 1
start = dt()
limit = 10**6
primes = f.prime_list(limit)
count = 0 
for i in range(1, len(primes)):
    p = primes[i]
    count += 2 * numSols((p*p - 1)//2)
print(count)
end = dt()
f.print_time_taken(start, end)

     
    