#sqrt(L**2 - (b/2)**2) is an integer
#b = h+1 or b = h-1 --> (h, h+1/2, L) is a pythagorean triple or (h, h-1/2, L) is a pythagorean triple
# (m^2 - n^2, 2mn, m^2 + n^2), and m^2 - n^2 = 4mn + 1 or m^2 - n^2 = 4mn - 1
# m^2 - 4mn - n^2 + 1 = 0 or m^2 - 4mn - n^2 - 1 = 0
# m = 4n +- sqrt(16n^2 + 4n^2 +- 4) / 2 = 2n + sqrt(5n^2 +- 1)
# need n such that 5n^2 +- 1 is a square number 
# 5n^2 +- 1 = k^2
# k^2 - 5n^2 = +-1
# pell's equation
# (k-sqrt(5)n)(k+sqrt(5)n) = -1, k = 2, n = 1 
# (x-sqrt(5)y)(2-sqrt(5)) = (2x + 5y - (2y+x)sqrt(5))
total = 0
k, n = 2, 1
for i in range(12):
    m = k + 2*n
    total += m*m + n*n
    k,n = 2*k + 5*n, 2*n + k
print(total)