def check(m,n): #m rows, n columns
    #need to create syseq 
    syseq = []
    output_vector = []
    for x1 in range(m):
        for y1 in range(n):
            eq = []
            numadjacent = 0
            for x2 in range(m):
                for y2 in range(n):
                    if x2 == x1 - 1 and y1 == y2:
                        numadjacent += 1
                        eq.append(1)
                    elif x2 == x1 + 1 and y1 == y2:
                        numadjacent += 1
                        eq.append(1)
                    elif y2 == y1 - 1 and x1 == x2:
                        numadjacent += 1
                        eq.append(1)
                    elif y2 == y1 + 1 and x1 == x2:
                        numadjacent += 1
                        eq.append(1)
                    else:
                        eq.append(0)
            if numadjacent % 2 == 1:
                eq[x1 * n + y1] = 1
            output_vector.append(numadjacent%2)
            syseq.append(eq)
    #solve system of equations
    #remember to xor
    #row reduce
    pivots = []
    for i in range(len(syseq)):
        eq = syseq[i]
        pivot = 0 
        while eq[pivot] == 0:
            pivot += 1
            if pivot == len(syseq):
                break
        if pivot == len(syseq):
            break
        pivots.append(pivot)
        for j in range(len(syseq)):
            if j != i and syseq[j][pivot]:
                for k in range(len(syseq)):
                    syseq[j][k] = syseq[j][k] ^ eq[k]
    return 1 << m*n - len(pivots)
print(check(14,210))
