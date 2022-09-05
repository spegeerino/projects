import functions as f
import timeit
#dominating numbers
#could do more combo stuff to improve runtime but lazy
def check_dominating(n):
    digits = [int(i) for i in str(n)]
    for i in range(10):
        frqcy = 0
        for d in digits:
            if d == i:
                frqcy += 1
        if frqcy > len(digits)//2:
            return True
    return False
def naive_sol(n):
    max = 10 ** n
    count = 0
    for i in range(1, max):
        if check_dominating(i):
            count += 1
    return count

def d(n, mod):
    '''number of n digit numbers that are dominating
    digits 1-9 are fundamentally same, 0 is weird though
    '''
    if n == 0:
        return 0
    required = (n>>1) + 1
    out = 0
    #1-9
    for i in range(required, n + 1):
        #if first digit is the dominator
        x = f.binom(n-1, i-1, mod)
        x *= pow(9, n-i, mod)
        x %= mod
        #if first digit is not the dominator
        if i != n:
            y = f.binom(n-1, i, mod)
            y *= 8
            y *= pow(9, n-i-1, mod)
            y %= mod
            x += y
        #multiply by 9 for 9 poss dominators
        x *= 9
        # print("1-9", i,x)
        out += x
        out %= mod
    #0
    for i in range(required, n):
        #first digit cannot be 0, so first digit is nonzero
        #if first digit is not the dominator
        x = f.binom(n-1, i, mod)
        x *= pow(9, n-i, mod)
        x %= mod
        out += x
        # print("0", i, x)
    return out % mod
stop = 2022
count = 0
mod = 1000000007
start = timeit.default_timer()
for i in range(1, stop + 1):
    if i % 20 == 0:
        print(i)
    count += d(i,mod)
end = timeit.default_timer()
print("done")
print(count % mod)
f.print_time_taken(start, end)

