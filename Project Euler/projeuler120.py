#define r(a,n) = (a-1)^n + (a+1)^n mod a^2
#find sum over max r(a,n) for 3 <= a <= 1000
#(a-1)^2 = 1-2a mod a^2, (a+1)^2 = 1+2a mod a^2, sum = 2 mod a^2
#(1-2a)(a-1) = 3a - 1 mod a^2, (1+2a)(a+1) = 3a + 1 mod a^2, sum = 6a mod a^2
#(3a-1)(a-1) = 1 - 4a mod a^2, (1+3a)(a+1) = 4a + 1 mod a^2, sum = 2 mod a^2
# 2a, 6a, 10a, 14a ... 
# def rmax(a):
#     return a * (a-2 + (a & 1))

# total = 0
# for i in range(3, 1001):
#     total += rmax(i)
# print(total)
print(sum([a*(a-2+(a&1))for a in range(1001)]))
# could reduce two sums to clean forms:
#sum over odd a from 3 to 999 of a(a-1) is like double every even index triangle number from 2 to 998, which has second difference 4, first difference 3
#0,3,10,21,36,55...
#3,7,11,15,19
#4,4,4,4