#parameterize numbers equal to the sum of n consecutive squares n > 1
# x^2 + (x+1)^2 = 2x^2 + 2x + 1
# x^2 + (x+1)^2 + (x+2)^2 = 3x^2 + 6x + 5
# x^2 + (x+1)^2 + ... + (x+n)^2 = (n+1)x^2 + n(n+1)x + n(n+1)(2n+1)/6, x > 0, n > 0
# x is limited by sqrt(A), n is limited by cbrt(A), O(n^5/6)
import math as ma
def check_palindrome(n):
    return n == reverse(n)

def reverse(n):
    out = 0
    while n > 0:
        out *= 10
        out += n % 10
        n //= 10
    return out

def sum_of_squares_1_to_n(n):
    return n * (n+1) * (2*n+1) // 6

def sum_of_squares_a_to_b(a,b):
    return sum_of_squares_1_to_n(b) - sum_of_squares_1_to_n(a-1)

total = 0
count = 0
limit = 10 ** 8 
palindrome_set = set()
for i in range(1, limit):
    if 2*i*i > limit:
        print(i)
        break
    for j in range(i+1, limit):
        test = sum_of_squares_a_to_b(i, j)
        if test >= limit:
            break
        if check_palindrome(test):
            if test in palindrome_set:
                print("DUPLICATE LMAO YOU THOUGHT YOU COULD WRITE CODE")
            palindrome_set.add(test)
            count += 1
            total += test
            print((test, i, j))
print("-----------")
print(total)
print(sum(palindrome_set))
print(count)
print(len(palindrome_set))
