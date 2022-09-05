import functions as f
modulus = 1000000007
def fibogen(n):
    #yields from f2 to fn inclusive
    x = 1
    y = 0
    for _ in range(n-1):
        temp = x
        x += y
        y = temp
        yield x

def better_S(k):
    #add k so that s(n) looks like (2,3,4,5,6,7,8,9,10),(20,30,40,50,60,70,80,90,100), 200...
    if k <= 9:
        return k*(k+1)//2
    #-1 + sum 45*10^i where i is from 0 to k//9
    #modularizing 
    geo_ub = k//9  # geo_ub = k//9 this is a power, need to do mod modulus - 1
    geo_ub %= modulus - 1
    total = -k
    total += 6 * (pow(10, geo_ub, modulus)-1) # total += 6 * (10**geo_ub-1) # 54(1 + 10)
    total %= modulus 
    leftover_nums = k % 9
    leftover_nums += 1
    total += (leftover_nums * (leftover_nums + 1)//2 - 1) * pow(10, geo_ub, modulus) # total += ((leftover_nums) * (leftover_nums+1)//2 - 1) * (10**geo_ub)
    return total % modulus

print(better_S(20))
total = 0
for i in fibogen(90):
    total += better_S(i)
    total %= modulus
print(total)