def nimsum(a,b,c):
    return a ^ (b ^ c)

count = 0
for i in range(1,2 ** 30 + 1):
    if i % 10000000 == 0:
        print(i)
    if not nimsum(i, i << 1, i + (i << 1)):
        count += 1

print(count) 