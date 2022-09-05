# notice that (sqrt(q) + sqrt(p))^2n + (sqrt(q) - sqrt(p))^2n is always integer
# therefore if sqrt(q) - sqrt(p) < 1, the second term will go to 0 (from positive)
# this will make the fractional part of the other term go to 1 as desired 
# then we use logs to figure out minimal error 
from numpy import log10, sqrt, floor, ceil
total = 0
import functions as f
for p in range(2, 10):
    upper = p + 1 + floor(2*sqrt(p))
    upper = min(int(upper), 2011 - p)
    for q in range(p+1, upper + 1):
        if not (f.is_square(q) and f.is_square(p)):
            print(p,q)
            red_rate = 2*log10(sqrt(q) - sqrt(p))
            min_n = ceil(-2011/red_rate)
            total += int(min_n) 
            print(total)
print(total)

