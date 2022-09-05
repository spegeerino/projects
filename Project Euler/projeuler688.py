from math import sqrt, floor
from timeit import default_timer as dt
from functions import print_time_taken as ptt
N = 10 ** 16 
upper = floor((sqrt(1 + 8*N) - 1) / 2) #inclusive
sum = 0
mod = 1000000007
start = dt()
print(upper)
for k in range(1, upper + 1):
    #sum f(i,k) from i = 1 to N
    #for i >= k(k+1)/2 f(i,k) >= 1 
    #for i >= k(k+3)/2 f(i,k) >= 2
    #for i >= k(k+2x-1)/2 f(i,k) >= x
    # sum n - k(k+2x-1)/2 + 1 for 1 <= x and k(k+2x-1)/2 <= n
    # sum n+1 - k^2/2 + k/2 - xk 
    # x(n+1) - xk^2/2 + xk/2 - x(x+1)k/2
    # x(n+1) - xk(x+k)/2 
    #n/k - (k-1)/2 >= x 
    x = floor(N/k - (k-1)/2)
    to_add = x*(N+1) - (x*k*(x+k)>>1)
    if k % 10**6 == 0:
        print(k)
        ptt(start, dt())
    sum += to_add  #sum k(k+2j-1)/2 for 1 <= j <= x
    sum %= mod
end = dt()
print(sum)
ptt(start, end) 