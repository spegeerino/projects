#4^t = 2^t + k => x^2 - x - k = 0, k = n(n-1) for some integer n > 1
#t can be real, but 4^t and 2^t must be integer
#we have t integer when k = 2^k(2^k-1)
#essentially we need floor(sqrt(n)) - 1 / log_2(n) - 1 = 1/12345
import timeit
import functions as f
start = timeit.default_timer()
def msb(n):
    i = 0
    while n > 0:
        i += 1
        n = n >> 1
    return i

for i in range(2,1000000):
    perfect = msb(i) - 1
    if perfect / (i-1) < 1/12345:
        print(i)
        print("answer: " + str(i*(i-1)))
        break
end = timeit.default_timer()
f.print_time_taken(start,end)