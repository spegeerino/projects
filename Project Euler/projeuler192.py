import math
notsquares = []
squares = [i ** 2 for i in range(2, 320)]
for i in range(2,100001):
    if i not in squares:
        notsquares.append(i)
#need SEMI CONVERGENTS as well, will do later because work
def eval_cont_frac(cont_frac):
    #output x,y where the evaluation is x/y
    x = 0
    y = 1
    for i in range(len(cont_frac) - 1, -1, -1):
        a_i = cont_frac[i]
        newy = a_i * y + x
        x = y
        y = newy
    temp = x
    x = y
    y = temp
    return (x,y)
denom_limit = 10 ** 12
total = 0
def best_semi_convergent(cont_frac):
    pass
for D in notsquares: 
    continued_fraction = []
    maxremovable = (int)(math.sqrt(D))
    a = maxremovable
    numer2 = a
    denom = D - numer2 * numer2
    continued_fraction.append(a)
    x,y = eval_cont_frac(continued_fraction)
    prevx, prevy = x,y
    desired = x * x - D * y * y
    while y <= denom_limit:
        # gotta find continued fraction expansion of sqrt(D)
        # sqrt(D) = a + sqrt(D) - a = a + (1 / (1 / (sqrt(D) - a) ) )
        # sqrt(D) = a + (1 / ( (sqrt(D) + a) / (D - a^2) )
        # new a_n+1 is such that sqrt(D) + a - a_n+1(D-a^2) is minimal positive
        # PROBLEM: denom isn't being reduced when it should be... how the fuck do i fix that, nvm i fixed it
        a = (numer2 + maxremovable) // denom 
        continued_fraction.append(a)
        numer2 = denom * a - numer2
        denom = (D - numer2 * numer2) // denom
        prevx, prevy = x, y
        x,y = eval_cont_frac(continued_fraction)
        desired = x*x - D*y*y
    total += prevy
    if D % 1000 == 0:
        print(D)
        print(x/y)
print(total)
