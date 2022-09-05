#literally just stealing the code from 114, this problem is super easy with 114 sol
limit = 10 ** 6
a = [1,1,1]
b = [0,0,0]
m = 50
while a[-1] + b[-1] <= limit:
    a_i = a[-1] + b[-1]
    b_i = 0
    for j in range(0, len(a) - m + 1):
        b_i += a[j]
    a.append(a_i)
    b.append(b_i)
print(a[-1] + b[-1])
print(len(a) - 1)