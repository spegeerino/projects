from functions import pf, pf_product, pf_num_of_divisors
small = pf(1)
big = pf(2)
t = pf_product(small, big)
t[2] -= 1
i = 2
limit = 500
while pf_num_of_divisors(t) <= limit:
    small = dict(big)
    big = pf(i+1)
    t = pf_product(small, big)
    t[2] -= 1
    i += 1
print(i*(i-1)//2)