#bro how many recurrence relations can i do
import functools
@functools.cache
def recur(n):
    #base cases
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 4
    if n == 4:
        return 8
    return recur(n-1) + recur(n-2) + recur(n-3) + recur(n-4)
print(recur(50))