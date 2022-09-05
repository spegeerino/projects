#surface area grows with square of side lengths, use finite differences
# volume of 0th layer (cuboid), volume of first layer, volume of second layer, volume of third layer?
# abc, 2ab + 2bc + 2ca, 2(a+2)(b+2) - 8 + c(2a + 2b + 4) = 2ab + 2bc + 2ca + 4a + 4b + 4c, 2(a+4)(b+4) - 24 + 2c(a + 4 + b) = 2ab + 2bc + 2ca + 8a + 8b + 8c + 8 
# 2ab + 2bc + 2ca - abc, 4a + 4b + 4c, 4a + 4b + 4c + 8
# abc - 2ab - 2bc - 2ca + 4a + 4b + 4c = (a-2)(b-2)(c-2) + 8, 8
# new method
# 4(n-1)^2 + 4(n-1)(a+b+c+1) + 2(ab + bc + ca) = 4n^2 - 8n + 4 + 4n(a+b+c+1) - 4(a+b+c+1) + 2(ab + bc + ca)
# 4n^2 + 4(a+b+c-1)n + (2ab + 2bc + 2ca - 4a - 4b - 4c)

def func(a,b,c,n):
    c_2 = 4
    c_1 = 4*(a+b+c-1)
    c_0 = 2*a*b + 2*b*c + 2*c*a - 4*a - 4*b - 4*c
    return c_0 + c_1 *n + c_2 * n*n
    #3, 3, 1 --> 9 + 21n - n(n-1)/2 = -n^2/2 + 43n/2 + 9: wrong
    #3, 2, 1 --> 6 + 16n + 8n(n-1)/2 = 4n^2 + 12n + 6; 6, 22, 
    #

vals = {}
limit = 100
for a in range(1,limit+1):
    print(a)
    for b in range(1, a+1):
        for c in range(1, b+1):
            n = 1
            x = func(a,b,c,n)
            while x <= limit * 4:
                if x in vals.keys():
                    vals[x] += 1
                else:
                    vals[x] = 1
                n += 1
                x = func(a,b,c,n)
for n in vals:
    if vals[n] >= 10:
        print(n, vals[n])
