import functions as f
import timeit
myn = 10**15
mymod = f.factorial(15)
def fast_fib(n, mod): 
    x = [1, 0]
    fib_iter = [[1, 1], [1, 0]] #fib_iter^1
    #generate a list of fib matrices raised to power 2^k
    fib_list = []
    for i in range(msb(n)):
        fib_list.append(fib_iter)
        fib_iter = matrix_square(fib_iter, mod)
    for i in range(msb(n)):
        two_pow = 1 << i
        if n & two_pow:
            x = vector_matrix_mul(x, fib_list[i], mod)
    return x[1]

def msb(n):
    x = 0 
    while n > 0:
        n >>= 1
        x += 1
    return x

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

fib_iter = [[1, 1], [1, 0]]
start_time = timeit.default_timer()
print(fast_fib(myn, mymod))
end_time = timeit.default_timer()
f.print_time_taken(start_time,end_time)