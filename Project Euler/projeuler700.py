import functions as func
import numpy as np


def naiveSum(a,b):
    lastEulerCoin = np.gcd(a,b)
    total = 0
    current = 0
    smallest = b
    for i in range(b):
        current += a
        current %= b
        if current < smallest:
            total += current
            smallest = current
            print((smallest,i+1))
        if current <= lastEulerCoin:
            break
    return total
multiplier = 1504170715041707
mod = 4503599627370517
def betterSum(a,b):
    print(a)
    total = a
    x = b
    y = a
    d = x - y
    while d > 0:
        num = y
        for _ in range(y//d):
            num -= d
            total += num
            print(num)
        if num == 0:
            break
        d = d - num
        y = num 
    return total

print("bettersum " + str(betterSum(multiplier,mod)))