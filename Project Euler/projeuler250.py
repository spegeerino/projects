mod = 10 ** 16

def poly_times(p, q):
    out_len = min(250, len(p) + len(q) - 1)
    out = [0] * out_len
    for i in range(len(p)):
        for j in range(len(q)):
            index = (i + j) % 250
            out[index] += (p[i] * q[j]) % mod
            out[index] %= mod
    return out

poly_square = lambda p: poly_times(p,p)

def poly_power(p, exp):
    mul_poly = p
    out = [1] 
    while exp > 0:
        if exp % 2 == 1:
            out = poly_times(out,mul_poly)
        exp //= 2
        mul_poly = poly_square(mul_poly)
    return out

res_cls_a = [0] * 250
res_cls_b = [0] * 250
poly_a = [0] * 250
poly_b = [0] * 250
for i in range(1, 501):
    index = pow(i, i, 250)
    res_cls_a[index] += 1

for i in range(1, 251):
    index = pow(i, i, 250)
    res_cls_b[index] += 1

def create_poly():
    out = [1] 
    for i_r in range(250):
        p = [1]
        p.extend([0] * i_r)
        p[-1] += 1
        p = poly_power(p, res_cls_a[i_r])
        out = poly_times(out, p)
    out = poly_power(out, 500)
    for i_r in range(250):
        p = [1]
        p.extend([0] * i_r)
        p = poly_power(p, res_cls_b[i_r])
        out = poly_times(out, p)
    return out 
print(create_poly()[0] - 1)
