# going to use pell's
# need to solve for error term in x^2 - ny^2 = 1 
# approx of sqrt n = x/y = s, s^2 - n = 1/y^2 implies y needs to be what 10^(101/2) to have acceptable error?
# this might be slow af but pell's should grow exponentially so hopefully not too bad?
# probably around like 1000 iterations per number, and there's only 100
import functions as f
import math as ma
def pell_iteration(state_list):
    a,b,n = state_list
    '''a and b are numer and denom, n is sqrt to approximate'''
    return [a + n*b, a+b, n]

def digits_to_string(digits):
    out_string = str(digits[0]) + "."
    for i in range(1,len(digits)):
        out_string += str(digits[i])
    return out_string
total = 0
for i in range(2, 100):
    if not f.is_square(i):
        state = (1,1,i)
        # separator
        while state[1] < 10**1250: #god i love python
            state = pell_iteration(state)
        #now need to find first 100 decimal digits sum
        digits = []
        a = state[0]
        b = state[1]
        for x in range(100):
            digits.append(a//b)
            a = a % b
            a *= 10
        total += sum(digits)
print(total)

