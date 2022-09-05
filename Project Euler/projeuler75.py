#parameterization is a = m^2 - n^2, b = 2mn, c = m^2 + n^2 for 0 < n < m
#sum is 2m(m+n)
#if gcd(m,n) == 1 and exactly one of m,n is even then we have primitive pythagorean triple
import functions as f
limit = 1500000
upper = 900
tracker = []
for m in range(1, upper):
    for n in range(1 + (m%2), m, 2):
        if(f.gcd(m,n) == 1):
            val = 2*m*(m+n)
            if val > limit:
                break
            tracker.append(val)
count = 0
nums = [0] * (limit + 1)
for i in tracker:
    for j in range(i, limit + 1, i):
        nums[j] += 1
for i in range(len(nums)):
    if nums[i] == 1:
        count += 1
        if count < 50:
            print(i)
print(count)