# here we just need more big integer stuff:
from projeuler013 import big_integer
x = big_integer("1")
power = 1000
for _ in range(power):
    x += x
print(sum([int(c) for c in str(x)]))
