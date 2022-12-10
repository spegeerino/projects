def d(n, x):
    # returns nth decimal digit of 1/x 
    rem = pow(10, n-1, x)
    rem *= 10
    return rem // x

def S(n):
    out = 0
    tc = 10 ** 5
    for i in range(1, n + 1):
        if (i % tc == 0):
            print(i)
        out += d(n, i)
    return out 

print(S(7))
print(S(100))
print(S(10**7))