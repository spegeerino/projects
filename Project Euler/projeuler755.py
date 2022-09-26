#S(10^13) is essentially # of subsets of fibonacci numbers that sum to <= 10^13
#first n fibonacci numbers sum to f_{n+2} - 2 (since we don't double count 1)
#so if we find the n fibonacci nums under 10^13, we can immediately add 2^(n-2)
#then branch by subtracting largest and second largest fibonacci num and continue downwards
from functools import cache

def fib_nums_under(n):
    #up to and including n
    out = []
    x = 1
    y = 1
    while x <= n:
        out.append(x)
        x,y = x+y, x
    return out

# {1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144}
@cache 
def S(n):
    if n < 0:
        return 0
    if n <= 1:
        return n+1
    fib_nums = fib_nums_under(n+2)
    out = 2 ** (len(fib_nums) - 2) #any subset of fibonacci nums from everything except last two is valid
    # print(f"S({n}) = {out} + S({n-fib_nums[-1]}) + S({n-fib_nums[-2]})")
    out += S(n - fib_nums[-1])
    out += S(n - fib_nums[-2]) - S(n - 2 * fib_nums[-2]) # can't duplicate f_n-2
    return out

@cache
def f_bounded(n, k):
    if n < 0:
        return 0
    if n == 0:
        return 1
    if n == 1 and k > 0:
        return 1
    fib_nums = fib_nums_under(min(n,k))
    if sum(fib_nums) < n:
        return 0 
    out = 0
    for k in fib_nums:
        out += f_bounded(n-k, k-1)
    return out

def naive_S(n):
    out = 0
    f = lambda n: f_bounded(n,n)
    for i in range(n+1):
        out += f(i)
    return out

print(S(10**13))


