# nums that can be written as (2a+1)^2 - (2b+1)^2 or (2a)^2 - (2b)^2
count = 0
limit = 10**6
for i in range(1,limit//4 + 10):
    for j in range(i-2, 0, -2):
        x = i*i - j*j
        if x > limit:
            break
        else:
            count += 1
print(count)