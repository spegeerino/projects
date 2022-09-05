import functions as f
#G(10) = 23044331520000
print(f.pf(23044331520000))
print(23044331520000)
ans = 1
n = 10
for i in range(2, 11):
    factor = i ** (n-i - (n-i)//i)
    ans *= factor
print(ans)
print(f.pf(ans))
