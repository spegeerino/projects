next_collatz = lambda n: 3*n + 1 if n%2 else n//2
limit = 10 ** 6
dp = [0] * limit
dp[1] = 1
largest = 0
best = 0
for i in range(2, limit):
    count = 0
    x = i
    while x >= limit or dp[x] == 0:
        x = next_collatz(x)
        count += 1
    dp[i] = dp[x] + count
    if largest < dp[i]:
        largest = dp[i]
        best = i
print(best)
