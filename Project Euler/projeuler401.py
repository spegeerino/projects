from math import sqrt
limit = 10 ** 15
mod = 10 ** 9

def oldsigma2(N):
    out = 0
    for i in range(1, N + 1):
        out += N // i * i * i 
    return out % mod
def SIGMA2(N):
    out = 0
    halfpower = (sqrt(N))
    for i in range(1, int(halfpower)+1):
        out += sumofsquares(N//i)
    for i in range(1, int(N/halfpower) + 1):
        out += N//i * i * i
    out -= int(halfpower) * sumofsquares(int(N/halfpower))
    return out % mod
def sumofsquares(b):
    return b * (b+1) * (2*b+1) // 6 

print(SIGMA2(limit))