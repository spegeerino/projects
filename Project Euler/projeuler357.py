from math import prod
import functions as f
import numpy as np
best_limit = 10 ** 8
time_check = 10 ** 6
# with open("primes.txt","r") as primes_file:
#     global primes
#     primes = []
#     while True:
#         try:
#             y = primes_file.readline()
#             x = int(y)
#             primes.append(x)
#         except:
#             break
# print("primes read")
# prime_set = set(primes)

# def binoflength(l):
#     max = 1 << l
#     for i in range(max):
#         x = i
#         out = []
#         while x > 0:
#             out.append(x&1)
#             x = x >> 1
#         while len(out) < l:
#             out.append(0)
#         yield out

#sum of all factor pairs = prime
#only need to consider pairs with all distinct factors, just choose which primes of factorization to give to which 
# only squarefree numbers
#sum of all such nums <= limit
#num must be 2 mod 4
#num must be product of at least two primes of multiplicity 1 (except for 2)
#include 2, include 3, include 5, include 7...
#2*3*5*7*11*13*17*19*23 > 10**8, max count is 8
#2 works, all others fail for one prime
#2 must be a factor of n

def generate_factor_pairs(prime_list):
    
for i in range(2, best_limit, 4):
    works = True
    if not f.is_prime(i+1):
        works = False
    if works:
        i_pf = f.pf(i)
        for v in i_pf.values():
            if v > 1:
                works = False
                break
    if works:
        i_pf_list = list(i_pf.keys())
        for pair in generate_factor_pairs(i_pf_list):



                
