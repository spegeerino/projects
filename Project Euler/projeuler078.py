import functions as f
#pentagonal numbers
pentagonal = lambda x: x * (3*x-1) // 2
# pentagonal(k) < pentagonal(-k), |3k-1| < |-3k-1| for pos k
# pentagonal(-k) < pentagonal(k+1), |3k+2| > |-3k-1| and |k+1| > |k| for pos k
# 
partitions = [1]
limit = 10**6
for i in range(1,limit + 1):
    if i % 10000 == 0:
        print(i)
    total = 0
    for k in range(1, i+1):
        a = pentagonal(k)
        b = pentagonal(0-k)
        factor = 2*(k&1) - 1
        if a > i:
            break
        total += partitions[i-a]*factor
        # total %= limit
        if b > i:
            break
        total += partitions[i-b]*factor
        # total %= limit
    if i == 25:
        print(partitions[i-1])
    if total % limit == 0:
        print(i)
        print(total)
    partitions.append(total % limit)





