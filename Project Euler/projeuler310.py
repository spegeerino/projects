# nim square, 3 heap normal play can remove square nums only
from math import isqrt
from timeit import default_timer as dt
from functions import print_time_taken as ptt
def lmpi(arr): # least missing positive integer
    for i in range(len(arr)):
        curr = abs(arr[i])
        if (curr <= len(arr)):
            arr[curr-1] = -abs(arr[curr-1])
    out = 1
    for i in range(len(arr)):
        if arr[i] < 0:
            out += 1
        else:
            return out
    return out

def trim_trailing_zeros(arr):
    out = []
    nonzero = False
    for i in arr[::-1]:
        if i != 0:
            nonzero = True
        if nonzero:
            out.insert(0, i)
    return out 

LIMIT = 10 ** 5
dp = [0] + LIMIT * [-1]
nimbers = [0] * (isqrt(LIMIT) + 2)
nimbers[0] = 1
start = dt()
for i in range(1, LIMIT + 1):
    j = 1
    moves = set()
    found_zero = False
    while (j*j <= i):
        x = dp[i - j*j]
        if x == 0:
            found_zero = True
        else:
            moves.add(x)
        j += 1
    if found_zero:
        dp[i] = lmpi(list(moves))
    else:
        dp[i] = 0
    nimbers[dp[i]] += 1
nimbers = trim_trailing_zeros(nimbers)
print(nimbers)
countP = 0
countN = 0
for c in range(len(nimbers)):
    for b in range(c + 1):
        for a in range(b + 1):
            x = a ^ b ^ c
            if (a != b and b != c):
                y = nimbers[a] * nimbers[b] * nimbers[c]
            elif (a == b and b != c):
                y = (nimbers[b]) * (nimbers[b] + 1) // 2
                y *= nimbers[c] 
            elif (a != b and b == c):
                y = (nimbers[b]) * (nimbers[b] + 1) // 2
                y *= nimbers[a]
            else:
                y = (nimbers[b]) * (nimbers[b] + 1) * (nimbers[b] + 2) // 6
            if x == 0:
                countP += y
            else:
                countN += y
print(countP, countN + countP)
end = dt()
print("done")
ptt(start, end)
# find one heap sols
 
