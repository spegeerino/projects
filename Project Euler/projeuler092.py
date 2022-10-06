from functions import digits
limit = 10 ** 7
dp = [-1] * limit
dp[1] = 1
dp[89] = 89
count = 0
def square_sum(n):
    return sum([x*x for x in digits(n)])
for i in range(1, limit):
    if i % (limit // 100) == 0:
        print(i)
    if dp[i] == -1:
        to_update = []
        x = i
        while dp[x] == -1:
            to_update.append(x)
            x = square_sum(x)
        for j in to_update:
            dp[j] = dp[x]
    if dp[i] == 89:
        count += 1
print(count)
            
