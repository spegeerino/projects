#f(n) for C(n^n)
from numpy import log2
from functions import print_time_taken
from timeit import default_timer as timer
def f(n):
    prime_file = open("primes.txt", "r")
    filestring = prime_file.readline()
    fileint = int(filestring)
    loglim = n * log2(n)
    primes = []
    print(loglim)
    while fileint <= loglim:
        primes.append(fileint)
        filestring = prime_file.readline()
        if not filestring:
            break
        fileint = int(filestring)
    print('primes read')
    p_i = 0
    count = 0
    q_index = 1
    firstfail = False
    notprinted = True 
    while not firstfail:
        if p_i % 10 == 0 and notprinted:
            print(p_i)
            notprinted = False
        p = primes[p_i]
        q = primes[q_index]
        loghn = p*log2(q) + q * log2(p)
        if loghn > loglim:
            if p_i + 1 == q_index:
                firstfail = True
            else:
                notprinted = True
                p_i += 1
                q_index = p_i + 1
        else:
            count += 1
            q_index += 1
    return count

def binsearchf(n):
    prime_file = open("primes.txt", "r")
    filestring = prime_file.readline()
    fileint = int(filestring)
    loglim = n * log2(n)
    primes = []
    print(loglim)
    while fileint <= loglim:
        primes.append(fileint)
        filestring = prime_file.readline()
        if not filestring:
            break
        fileint = int(filestring)
    print('primes read')
    p_i = 0
    count = 0
    checker = primes[p_i] * log2(primes[p_i + 1]) + primes[p_i + 1] * log2(primes[p_i])
    while checker < loglim:
        p = primes[p_i]
        #need plogq + qlogp <= loglim: binary search
        l = p_i + 1
        r = len(primes)
        while r >= l:
            m = (l + r) // 2
            q = primes[m]
            checkval = p*log2(q) + q*log2(p)
            if checkval > loglim:
                r = m-1
            else:
                l = m+1
        count += l - p_i - 1
        p_i += 1 
        checker = primes[p_i] * log2(primes[p_i + 1]) + primes[p_i + 1] * log2(primes[p_i])
    return count

start = timer()
print(binsearchf(800800))
end = timer()
print_time_taken(start, end)