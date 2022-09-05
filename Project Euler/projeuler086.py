from math import sqrt
import time
start_time = time.time()
count = 0
limit = 10 ** 6
def is_square(n):
    x = sqrt(n)
    return int(x+0.5) ** 2 == n
for i in range(1,10 ** 5):
    mcount = 0
    for y in range(2, 2*i + 1):
        if is_square(i*i + y*y):
            #y = j+k, j >= k, but j <= i so we need to count all legitimate js
            #for even j j can range from y//2 to min(i,y-1)
            #for odd j j can range from y//2 + 1 to min(i,y-1)
            need_to_add = min(i+1,y) - (y//2) - (y%2)
            mcount += need_to_add
    count += mcount
    if count > limit:
        print(i)
        break
print("elapsed: %s seconds" % (time.time() - start_time))