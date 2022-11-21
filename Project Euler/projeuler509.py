# divisor nim
from math import log2, floor

def S(n, mod):
    upper = floor(log2(n)) + 1
    nimbers = [n // (2 ** k) - n // (2 ** (k+1)) for k in range(upper)]
    nimbers = [i % mod for i in nimbers]
    print(nimbers)
    countP = 0
    countN = 0
    for a in range(len(nimbers)):
        for b in range(len(nimbers)):
            for c in range(len(nimbers)):
                if (a ^ b ^ c) == 0:
                    countP += nimbers[a] * nimbers[b] * nimbers[c]
                    countP %= mod
                else:
                    countN += nimbers[a] * nimbers[b] * nimbers[c]
                    countN %= mod
    return countN, countP

print(S(123456787654321, 1234567890))



