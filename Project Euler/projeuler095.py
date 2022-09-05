import functions as f
import timeit
start = timeit.default_timer()
def amic_len(n):
    previous = []
    while n not in previous:
        previous.append(n)
        n = f.sum_of_divisors(n) - n
        if n > 1000000 or n == 0:
            return 0
        if n == previous[0]:
            return len(previous)
    return 0
best = 0
bestnum = 0
for i in range(2, 1000000):
    x = amic_len(i)
    if x > best:
        best = x
        bestnum = i
        print((best,bestnum))
print(bestnum)
end = timeit.default_timer()
print("time taken: " + str(end - start) + "s")
