#a(0) = 1, b(0) = 0, a(1) = 1, b(1) = 1
#(a(n) + b(n)sqrt7)(1 + sqrt7) = [a(n) + 7b(n)] + [a(n) + b(n)]sqrt7
# a(n+1) = a(n) + 7b(n), b(n+1) = a(n) + b(n)
# [[1 7]]^n [1]   [a(n)]
# [[1 1]]   [0] = [b(n)]
# diagonalize? eigenvalues are 1 +- sqrt(7) obviously, eigenvectors are [-sqrt7, 1] and [sqrt7, 1]
# we get A = QDQ^-1 = [-sqrt7 sqrt7][1 + sqrt7     0    ][-1/2sqrt7 1/2]
#                     [  1      1  ][   0      1 - sqrt7][ 1/2sqrt7 1/2]