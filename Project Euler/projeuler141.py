#n is progressive if n = dq + r where d,q,r form a geometric sequence in some order
#we can assume 3 different forms: r is 1st term, 2nd term, 3rd term
#we get n = a^2b^3 + a, n = a^2b^2 + ab, n = a^2b + ab^2
#we also require n = k^2
#k^2 = ab(ab+1) 2nd case doesn't work, consecutive numbers can't multiply to a square
#r cannot be 3rd term because r < d
#therefore we only have k^2 = a^2b^3 + a as a valid parameterization
#can simply iterate along a and b to see if the output is a square
#no we can't because b could be not an integer, but so long as ab and ab^2 are integer it works
#so how do we find this if b could be rational
#don't want to find all prime factors with exp >= 2 in num because slow
#b > 1
import functions as f
import math as ma
import timeit
limit = 10 ** 5
# limit = 10 ** 12
nums = set()
start = timeit.default_timer()
for a in range(1, int(ma.sqrt(limit)/8)):
    apf = f.pf(a)
    l = [1]
    for k in apf.keys():
        if apf[k] >= 2:
            l.append(k)
    for b in range(2, int(ma.pow(limit, 1/2))):
        n = a*a*b*b*b + a
        if n >= limit:
            break
        if f.is_square(n):
            nums.add(n)
end = timeit.default_timer()
print(sum(nums))
print(nums)
print("time taken: " + str(end - start) + "s")