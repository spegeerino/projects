# this question is actually O(1): we have to go down 20 times and right 20 times in any order
# the order uniquely defines the path
# this means we need the permutations of "D" * 20 + "R" * 20, which is just (40 choose 20)
# in general the answer is (2n choose n)
from functions import binom
print(binom(40, 20)) 