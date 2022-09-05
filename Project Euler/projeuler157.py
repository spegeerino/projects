# want sols to 1/a + 1/b = k/10^n (a <= b)
# same as sols to (ka - 10^n)(kb - 10^n) = 10^2n
# can iterate over factor pairs of 10^2n, and the number of sols for that particular factor pair is #factors of gcd of those two factors
# need to write code to generate factor pairs 
import functions as f
from timeit import default_timer as dt
total = 0 
limit = 9
start = dt()
for n in range(1, limit + 1):
    for f2 in range(2*n+1):
        for f5 in range(2*n+1):
            TN = 10 ** n
            p = TN + pow(2, f2) * pow(5, f5)
            q = TN + pow(2, 2*n-f2) * pow(5, 2*n-f5)
            if p <= q:
                d = f.gcd(p,q)
                total += f.num_factors(d)
print(total)
f.print_time_taken(start, dt())

