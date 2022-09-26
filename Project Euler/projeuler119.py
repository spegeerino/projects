#let d(n) be the sum of the digits of n, we want n >= 10 such that n = d(n)^k for some k > 1
#in specific we want the 30th smallest such n
#we can try numbers for d(n) and raise them to powers until they are too large
#and see how many we get
from functions import sum_of_digits
A = []
num_digits = 15
limit = 10 ** num_digits
for d in range(2, 9*num_digits):
    x = d * d
    while x < limit:
        if sum_of_digits(x) == d:
            A.append(x)
        x *= d
A.sort()
print(A)
print(len(A))