#ok this is getting ridiculous p sure i can do states and recurrence relations again
#wait i don't even need states this is just fib - 1, delay1_fib - 1, and delay2_fib - 1
import functools
@functools.cache
def delay_fib(n, d):
    if n == 0:
        return 0
    if n <= d + 2:
        return 1
    return delay_fib(n-1, d) + delay_fib(n-2-d, d)
length = 50
print(delay_fib(length+1, 0) + delay_fib(length+1, 1) + delay_fib(length+1, 2) - 3)