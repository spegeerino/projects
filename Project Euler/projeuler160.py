def sol(n, d):
    x = 1
    mod = 10 ** d
    for i in range(1, n + 1):
        if i % 10**6 == 0:
            print(i)
        x *= i 
        while x % 10 == 0:
            x //= 10 
        x %= mod 
    return x
a = sol(100, 5)
b = sol(200, 5)
print(a, b)
print(a*a % 10**5)