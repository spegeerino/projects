#fib golden nuggets
#gen func is xf_1 + x^2f_2 + x^3f_3 + ... = x/(1 - x - x^2)
#we want x/(1-x-x^2) = N for some rational x
#-x = N(x^2 + x - 1) --> Nx^2 + (N+1)x - N = 0
#x is rational if sqrt((N+1)^2 + 4N^2) is rational
# 5N^2 + 2N + 1 = k^2 --> (N+1)^2 + (2N)^2 = k^2
# m^2 - n^2 = N+1, mn = N --> m^2 - mn - n^2 - 1 = 0 
# m = n + sqrt(n^2 + 4n^2 + 4) / 2
# m = n + sqrt(5n^2 + 4) / 2
# or m^2 - n^2 = N, mn = N + 1/2 --> DOES WORK
# n + sqrt(n^2 + 4n^2 + 2) --> sqrt(5n^2 + 2) is rational
# however, k^2 =/= 2 mod 5, doesn't work
# pell's again? ok
# sols to x^2 - 5n^2 = 4: x = 3, n = 1; double the numbers from any solution to x^2 - 5n^2 = 1
import functions as f
def pell_iter(k,n):
    return 9*k + 20*n, 9*n + 4*k 
# (9 + 4sqrt(5))(x + ysqrt(5)) = (9x + 20y) + (4x + 9y)sqrt(5)
#pell's sol = 9, 4
k1, n1 = 3, 1
k2, n2 = 18, 8 
k3, n3 = 7, 3
count_sols = 0
while count_sols < 15:
    count_sols += 1
    m1 = (n1+k1) // 2
    m2 = (n2+k2) // 2
    m3 = (n3+k3) // 2
    N1 = m1*n1
    N2 = m2*n2
    N3 = m3 * n3
    if N1 < N2:
        if N1 < N3:
            print(count_sols, N1)
            k1, n1 = pell_iter(k1, n1)
        else:
            print(count_sols, N3)
            k3, n3 = pell_iter(k3, n3)
    else:
        if N2 < N3:
            print(count_sols, N2)
            k2, n2 = pell_iter(k2, n2)
        else:
            print(count_sols, N3)
            k3, n3 = pell_iter(k3, n3)
    