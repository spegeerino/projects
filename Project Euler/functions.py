import math as m
import numpy as np

def gen_prime_sieve(upper):
    primes = []
    sieve = [True] * upper
    sieve[0] = False
    i = 1
    while i < m.sqrt(upper) + 1:
        if sieve[i]:
            n = i + 1
            primes.append(n)
            for k in range(n*n - 1, upper, n):
                sieve[k] = False
        i += 1
    while i < upper:
        if sieve[i]:
            primes.append(i+1)
        i += 1
    return primes

def gcd2(a,b):
    x = max(a,b)
    y = a+b-x
    while(y!=0):
        temp = y
        y = x - x//y * y
        x = temp
    return x

def gcd(*args):
    sofar = 0
    for arg in args:
        sofar = gcd2(arg, sofar)
    return sofar

def print_time_taken(start,end):
    print(f"Time elapsed: {end-start}s")

def reverse(n):
    x = 0
    while n > 0:
        x *= 10
        x += n % 10
        n //= 10
    return x

def digits(x):
    out = []
    while x > 0:
        out.insert(0,x%10)
        x = x // 10
    return out

def sum_of_digits(n):
    out = 0
    while n > 0:
        out += n % 10
        n //= 10
    return out

def list_gcd(x):
    out = x[0]
    for i in range(1, len(x)):
        out = gcd(out,x[i])
    return out

def list_copy(a):
    return list(a)

def figurate(n, sides = 3):
    '''returns the figurate numbers: by default we have 3 sided polygon = triangle numbers 1,3,6,10,15...
    4 sides would give the square numbers 1,4,9,16,25...
    5 sides would give the pentgonal numbers 1,5,12,22,35,...
    '''
    return n * ((sides - 2)*n + 4 - sides) // 2

def is_square(n):
    x = int(m.sqrt(n) + 0.5)
    return x*x == n

def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(m.sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True

def totient(n):
    x = pf(n)
    for k in x.keys():
        n = n // k
        n *= k-1
    return n

def is_prime_sieve(n,primes):
    if n == 1:
        return False
    for p in primes:
        if n % p == 0:
            return False
        if p > m.sqrt(n):
            return True
    return is_prime(n)

def fast_primes_test(x, bases):
    #this doesn't work at all
    # supposed to be based on fermat pseudoprimes (miller-rabin)
    out = True
    for b in bases:
        exp = x - 1
        while exp % 2 == 0:
            check = pow(b, exp, x)
            if check != 1:
                out = out and ((check % x) == x-1)
            exp //= 2
        check = pow(b, exp, x)
        out = out and (check == 1 or check == -1)
    return out

def next_prime(primes):
    i = primes[-1] + 1
    upper = m.isqrt(2*primes[-1]) #there is a prime between p and 2p for all p
    while True:
        valid = True
        for p in primes:
            if i % p == 0:
                valid = False
                break
            if p >= upper:
                break 
        if valid:
            return i
        i += 1
def prime_list_sieve(upper):
    out = [2]
    middle = int(m.sqrt(upper)) + 1
    for i in range(3,middle):
        valid = True
        for j in out:
            if i % j == 0:
                valid = False
                break
        if valid:
            out.append(i)
    stop = len(out)
    for i in range(middle,upper):
        valid = True
        for j in out[:stop]:
            if i % j == 0:
                valid = False
                break
        if valid:
            out.append(i)
    return(out)

def prime_list(upper):
    out = []
    for i in range(2,upper):
        if is_prime(i):
            out.append(i)
    return out

def mod_inverse(num, mod):
    '''
    >>> mod_inverse(9, 11)
    5
    >>> mod_inverse(20, 99)
    5
    >>> mod_inverse(7, 5)
    3
    >>> mod_inverse(12, 169)
    155
    '''
    assert num > 0, "works only with positive n mod m"
    assert mod > 0, "cannot have negative modulus"
    a = mod
    b = num % mod 
    prev_x, prev_y = 1, 0
    curr_x, curr_y = 0, 1 
    while b > 1:
        k = -(a // b)
        tx, ty = curr_x, curr_y #temp vars
        curr_x, curr_y = prev_x - k*curr_x, prev_y - k*curr_y
        prev_x, prev_y = tx, ty 
        a,b = b, a % b
    # we have ax - by = +-1, take negative to get -ax - by = -1, by = a(-x) + 1
    checker = curr_x * mod - curr_y * (num%mod)
    if checker == 1: 
        return mod - curr_y
    return curr_y 

    
def derangements(n):
    if n == 0: 
        return 1
    if n == 1:
        return 0 
    return (n-1) * (derangements(n-1) + derangements(n-2))

def pf(n):
    ''' returns the prime factorization of n as a dictionary'''
    def pf_helper(n, s):
        if n == 1:
            return {}
        for i in range(s, (int)(m.sqrt(n) + 1)):
            if n % i == 0:
                p_index = 0
                newnum = n
                while newnum % i == 0:
                    p_index += 1
                    newnum //= i
                out = pf_helper(newnum, i+1)
                out[i] = p_index
                return out
        return {n:1}
    return pf_helper(n, 2)

def pf_sieve(n,primes):
    if n == 1:
        return {}
    for p in primes:
        if n % p == 0:
            p_index = 1
            newnum = n//p
            while newnum % p == 0:
                p_index += 1
                newnum //= p
            out = pf(newnum)
            out[p] = p_index
            return out
    return None

def pf_inverse(pf):
    ''' edits a pf to flip the signs to do division'''
    for i in pf.keys():
        pf[i] = -1 * pf[i]
    return pf

def common_elements(a,b):
    a_set = set(a)
    b_set = set(b)
    return list(a_set & b_set)

def pf_product(a,b):
    out = {}
    for i in common_elements(a.keys(),b.keys()):
        out[i] = a[i] + b[i]
    for i in a.keys():
        if i not in out.keys():
            out[i] = a[i]
    for i in b.keys():
        if i not in out.keys():
            out[i] = b[i]
    badkeys = []
    for i in out.keys():
        if out[i] == 0:
            badkeys.append(i)
    for i in badkeys:
        out.pop(i)
    return out

def pf_eval(pf):
    '''returns product of prime factors of pf'''
    out = 1
    for i in pf.keys():
        out *= i ** pf[i]
    return out

def sum_of_divisors(n):
    return pf_sum_of_divisors(pf(n))

def pf_sum_of_divisors(pf):
    out = 1
    for p in pf.keys():
        x = 0
        a = 1
        for i in range(pf[p] + 1):
            x += a
            a *= p
        out *= x
    return out

def pf_num_of_divisors(pf):
    out = 1
    for p in pf.keys():
        out *= pf[p] + 1
    return out 

def num_factors(n):
    return pf_num_of_divisors(pf(n))

def factorial(n):
    if n < 0:
        return -1
    out = 1
    for i in range(2,n+1):
        out *= i
    return out

def pf_factorial(n):
    out = {}
    primes = prime_list_sieve(n)
    for i in primes:
        if i > n:
            return out
        x = i
        y = 0
        while x <= n:
            y += n // x
            x *= i
        out[i] = y
    return out

def binom(n,r, mod = 0):
    #mod must be prime 
    if r > n:
        return 0
    if mod == 0:
        out = 1
        for i in range(r+1, n+1):
            out *= i
        return out // factorial(n-r)
    out = 1
    for i in range(r+1, n+1):
        out *= i
        out %= mod
    denom = 1
    for i in range(1, n-r+1):
        denom *= i
        denom %= mod
    return out * pow(denom, mod-2, mod)

#edits matrix in place into row echelon form FIX THIS DOESN'T WORK
def row_echelon(matrix):
    num_rows = len(matrix)
    num_cols = len(matrix[0])
    offset = 0
    for i in range(num_rows):
        if matrix[i][i] != 0:
            #reduce row to 1 in first entry note this causes problem when matrix[i][i] = 0
            scalar = 1/matrix[i][i]
            for j in range(i,num_cols):
                matrix[i][j] *= scalar
            print(matrix[i])
            #remove all copies from other rows
            for j in range(i + 1, num_rows):
                copies_to_subtract = matrix[j][i]
                for k in range(i, num_cols):
                    matrix[j][k] -= copies_to_subtract * matrix[i][k]
            print(matrix[i])
    return matrix

def determinant(matrix):
    out = 1
    num_rows = len(matrix)
    num_cols = len(matrix[0])
    for i in range(num_rows):
        #reduce row to 1 in first entry
        scalar = 1/matrix[i][i]
        out *= matrix[i][i]
        #print(out)
        #print(matrix[i])
        for j in range(i,num_cols):
            matrix[i][j] *= scalar
        #remove all copies from other rows
        for j in range(i + 1, num_rows):
            copies_to_subtract = matrix[j][i]
            for k in range(i, num_cols):
                matrix[j][k] -= copies_to_subtract * matrix[i][k]
        
    return out

def dot_prod(v, w, mod):
    '''
    >>> dot_prod([1,2,3,4],[1,2,3,4],8)
    6
    >>> dot_prod([4,3,2,1],[1,2,3,4],3)
    2
    >>> dot_prod([6,7],[8,0],12)
    0
    '''
    out = 0
    for i in range(len(v)):
        out += v[i] * w[i]
        if mod:
            out %= mod
    return out 

def vector_matrix_mul(v, A, mod):
    '''
    Takes vector v of dim n and nxn matrix A, returns Av. 
    >>> vector_matrix_mul([13, 8], [[1, 1], [1, 0]], 10)
    [1, 3]
    >>> vector_matrix_mul([1, 1], [[1, 1], [1, 0]], 5)
    [2, 1]
    '''
    out = []
    for i in range(len(v)):
        #iter over terms in v
        out.append(dot_prod(A[i], v, mod))
    return out

def matrix_square(A, mod):
    '''
    takes nxn A and returns A^2
    >>> matrix_square([[1, 1], [1, 0]], 3)
    [[2, 1], [1, 1]]
    '''
    out = []
    for i in range(len(A)):
        out.append([])
        for j in range(len(A)):
            out[i].append(0)
    for i in range(len(A)):
        #each col of A^2 should be A(A_coli)
        A_coli = [A[j][i] for j in range(len(A))]
        A2_coli = vector_matrix_mul(A_coli, A, mod)
        for j in range(len(A)):
            out[j][i] = A2_coli[j]
    return out 

def msb(n):
    '''
    returns the largest nonnegative integer k such that n - 2^k >= 0
    >>> msb(3)
    1
    >>> msb(2)
    1
    >>> msb(103)
    6
    '''
    x = -1
    while n > 0:
        n >>= 1
        x += 1
    return x

def fast_fib(n, mod=0):
    '''use mod = 0 to have no mod'''
    x = [1, 0]
    fib_iter = [[1, 1], [1, 0]] #fib_iter^1
    #generate a list of fib matrices raised to power 2^k
    fib_list = []
    for i in range(msb(n)+1):
        fib_list.append(fib_iter)
        fib_iter = matrix_square(fib_iter, mod)
    for i in range(msb(n)+1):
        two_pow = 1 << i
        if n & two_pow:
            x = vector_matrix_mul(x, fib_list[i], mod)
    return x #x[0] = f_{n+1}, x[1] = f_n
    
def main():
   import doctest 
   doctest.testmod()

if __name__ == "__main__":
    main()