import functools

#game returns true if losing, false if winning
def nim(m,n):
    return m==n
@functools.lru_cache(maxsize = 10000)
def eq_nim(m,n):
    if m == 0 or m == n:
        return False
    remove_m = any([eq_nim(i, n) for i in range(1,m)])
    remove_n = any([eq_nim(min(i, m), max(i,m)) for i in range(1,n)])
    remove_both = any([eq_nim(m-i, n-i) for i in range(1,m)])
    return not(remove_m or remove_n or remove_both)
sum_lim = 50
for m in range(sum_lim):
    for n in range(m, sum_lim+1-m):
        if eq_nim(m,n):
            print(m,n)
            break
def prop_nim(m,n):
    pass
