import functions as f
is_palindrome = lambda n: n == f.reverse(n)
limit = 1000 
largest = 0 
for i in range(100, limit):
    for j in range(100, limit):
        prod = i*j
        if prod > largest and is_palindrome(prod):
            largest = prod
print(largest)