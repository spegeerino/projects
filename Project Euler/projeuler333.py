#ANSWER: unknown
# All positive integers can be partitioned in such a way that each and every term of the partition can be expressed as 2ix3j, where i,j ≥ 0.

# Let's consider only such partitions where none of the terms can divide any of the other terms.
# For example, the partition of 17 = 2 + 6 + 9 = (2^1x3^0 + 2^1x3^1 + 2^0x3^2) would not be valid since 2 can divide 6. 
# Neither would the partition 17 = 16 + 1 = (2^4x3^0 + 2^0x3^0) since 1 can divide 16. 
# The only valid partition of 17 would be 8 + 9 = (2^3x3^0 + 2^0x3^2).

# Many integers have more than one valid partition, the first being 11 having the following two partitions.
# 11 = 2 + 9 = (2^1x3^0 + 2^0x3^2)
# 11 = 8 + 3 = (2^3x3^0 + 2^0x3^1)

# Let's define P(n) as the number of valid partitions of n. For example, P(11) = 2.

# Let's consider only the prime integers q which would have a single valid partition such as P(17).

# The sum of the primes q <100 such that P(q)=1 equals 233.

# Find the sum of the primes q <1000000 such that P(q)=1.

#2^a - 2^b = 3^c - 3^d
#2^b(2^(a-b)-1) = 3^d(3^(c-d) - 1) let e = a-b and f = c-d
#2^b(2^e - 1) = 3^d(3^f - 1) = N, N = 2^b*3^d*K for some K

#sps K != 1: then gcd(2^e-1, 3^f - 1) = K, implying 2^e-1 = K3^d and 3^f - 1 = K2^b e = 4, f = 4, K = 5, b = 4, d = 1
#if i choose some K then i get 

limit = 10 ** 6

def first_partition(n):
    r = 0 #power of 2
    out = []
    while n > 0:
        while n & 1 == 0:
            n = n >> 1
            r += 1
        largest = 1
        while n >= largest:
            largest *= 3
        largest //= 3
        n -= largest
        twor = 1 << r
        out.append(twor * largest)
    return out

print(first_partition(14))
        
    
    
