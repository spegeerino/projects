#strong achilles numbers, nums such that p^2 | n for all p in n but n =\= a^b
import functions as f

def is_perfect_power(n):
    pf = f.pf(n)
    exponents = [i for i in pf.values()]
    return f.list_gcd(exponents) != 1

def is_powerful(n):
    pf = f.pf(n)
    return len([i for i in pf.values() if i == 1]) == 0

def is_achilles(n):
    return is_powerful(n) and not is_perfect_power(n)

limit = 10 ** 6
nums = []
for i in range(72,limit):
    if i % 100000 == 0:
        print(i)
    j = f.totient(i)
    if is_achilles(i) and is_achilles(j):
        nums.append(i)

print(nums)