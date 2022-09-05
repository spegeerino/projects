import functions as func
limit = 10 ** 8
count = 0
for i in range(1, limit + 1):
    if i % 1000 == 0:
        print(i)
    min_per = i*i << 1
    if min_per > limit:
        break
    for j in range(1 + (i % 2), i, 2):
        a = i*i - j*j
        b = 2*i*j
        c = i*i + j*j
        if a + b + c >= limit:
            break
        if c % abs(b-a) == 0 and func.gcd(i,j) == 1:
            addend = limit//(a+b+c)
            count += addend
        
print(count)
