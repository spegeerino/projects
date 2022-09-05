lower_bound = 1.00000000001
upper_bound = 1.01
DES_SUM = -6 * (10 ** 11)

#find real upper_bound

def func(r):
    output = 897
    output -= 900 * r
    output += 14103*pow(r,5000)
    output -= 14100*pow(r,5001)
    denom = pow(1-r, 2)
    output /= denom
    return output

print(DES_SUM - func(1.002322108632876))