# A window into a matrix is a contiguous sub matrix.

# Consider a 2 x n matrix where every entry is either 0 or 1.
# Let A(k,n) be the total number of these 2xn matrices such that the sum of the entries in every 2xk window is k.

# You are given that A(3,9) = 560 and A(4, 20) = 1060870.

# Find A(10^8, 10^16). Give your answer modulo 1 000 000 007.
# A(1,n) = 2^n
#----------------------------------------------------------------------------------
# we can assume that k divides n because that's true for all nums given
# then take the first 2xk window, its elements must sum to k
# there are 2 rows, each can have a value of max k, but they must total to k
# there are k+1 ways of doing this if we only care about the sums of each row
# then we permute the columns, which we'll need some combinatorial identity for
# sum_{i=0}^k of (k choose i) (k choose k - i) = (2k choose k)
# also notice that there are 2k entries and k of them must be 1 and the others are 0 so we also get (2k choose k) from that
# now suppose we move window over 1 to the right
# <first col is 0s>(2k-2 choose k) + <first col has sum 1>2(2k-2 choose k-1) + <first col has sum 2>(2k-2 choose k-2) 