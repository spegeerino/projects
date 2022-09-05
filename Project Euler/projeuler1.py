import functions as f
def sum_mul_k(n,k):
    return k * f.figurate(n//k)
limit = 1000 
print(sum_mul_k(limit - 1, 3) + sum_mul_k(limit - 1, 5) - sum_mul_k(limit - 1, 15))