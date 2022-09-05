#same thing as 137, just gotta change the numbers ok maybe not
#gen func of A_1 = 1, A_2 = 4, A_n = A_n-1 + A_n-2
# sum A_nx^n = x + 4x^2 + sum_n=3^infty A_nx^n = x + 4x^2 + xsum_n=2^\infty A_nx^n + x^2sum_n=1^\infty A_nx^N = x + 4x^2 + xA(x) - x^2 + x^2A(x)
# A(x) = x + 3x^2 / 1 - x - x^2
# x + 3x^2 = N(1 - x - x^2) --> (N+3)x^2 + (N+1)x + N = 0 --> sqrt((N+1)^2 + 4N^2 + 12N) is rational
# 5N^2 + 14N + 1 is perfect square: 5N^2 + 14N + 1 = k^2 
# seems like this is true if and only if k = A_i where i is 1 mod 4
# why?
import functions as f
from math import isqrt
def recur(n):
    if n == 0:
        return 3
    if n == 1:
        return 1
    if n > 1:
        return recur(n-1) + recur(n-2)
    return recur(n+2) - recur(n+1)

for i in range(-20, 20):
    print(recur(i))

print("-" * 60)
for i in range(1, 10000):
    if f.is_square(5*i*i + 14*i + 1):
        print(i, isqrt(5*i*i + 14*i + 1))