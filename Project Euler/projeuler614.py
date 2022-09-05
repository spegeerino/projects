mod = 10 ** 9 + 7
def gen_func_poly(limit):
    out = [0] * (limit + 1)
    out[0] = 1
    out[1] = 1
    for i in range(3, limit+1, 2):
        if i % (limit // 1000) == 1:
            print(i)
        for k in range(limit - i, -1, -1):
            out[k+i] = (out[k+i] + out[k]) % mod
    for i in range(4, limit+1, 4):
        if i % (limit // 1000) == 0:
            print(i)
        for k in range(limit - i, -1, -1):
            out[k+i] = (out[k+i] + out[k]) % mod
    return out

print(sum(gen_func_poly(10**7)) % mod)

