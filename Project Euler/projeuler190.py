#lagrange multipliers
import functions as f
def tn(n):
    return f.binom(n+1, 2)

total = 0
for m in range(2, 16):
    denom = tn(m)
    out = 1
    product = 1
    for n in range(1, m+1):
        val = m*n/denom
        val = pow(val, n)
        product *= val
    product = int(product)
    print("m:", product)
    total += product

print("ans:", total)
