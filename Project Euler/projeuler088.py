import functions as f
N = 12
maximum = 0
total = 0
def factor_sum(pf):
    out = 0
    for k in pf:
        out += k * pf[k]
    return out 
def factor_num(pf):
    out = 0
    for k in pf:
        out += pf[k]
    return out 
for i in range(4, 2*N + 1):
    i_pf = f.pf(i)
    sum_facs = factor_sum(i_pf)
    num_facs = factor_num(i_pf)
    num_facs += i - sum_facs
    if num_facs > maximum:
        total += i
        maximum = num_facs 
        print(i, num_facs)
    if maximum >= N:
        break 
print(total)


    
