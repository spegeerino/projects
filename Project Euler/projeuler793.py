def prng(n):
    seed = 290797
    mod = 50515093
    for _ in range(n):
        yield seed
        seed = pow(seed, 2, mod)

limit = 103
vals = list(prng(limit))
vals.sort()
print(vals[:5])