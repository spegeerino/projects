# a < c <= d < b
# a = l(k-l-1)
# b = l(k-l-1) + k
# c = l(k-l)
# d = l+1(k - l - 1)
# N = l(l+1)(k-l)(k-l-1) < 10 ** 14
# therefore t = l(k-l-1)
from math import sqrt
limit = 10 ** 14
def count_stealthy_numbers(max):
    nums = set()
    for k in range(3, int(sqrt(max))):
        rb = int((k-1) / 2)
        if k % 10000 == 0:
            print(k)
        for l in range(1,rb + 1):
            N = l * (l+1) * (k-l) * (k-l-1)
            if N <= max:
                nums.add(N)
            else:
                break
    return len(nums)
print(count_stealthy_numbers(limit))

