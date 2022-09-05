#R(k) = 10^k - 1 / (10-1)
import functions as f
desired = 10 ** 6
upper = 10 * desired 
for i in range(desired, desired + 172):
    if i % 2 == 0 or i % 5 == 0:
        continue 
    x = f.totient(i)
    totient_pf = f.pf(x)
    print(i)
    print(totient_pf)
    works = True 
    for k in totient_pf.keys():
        if k != 3 and pow(10, x//k, i) == 1:
            works = False
            break
    if works:
        print(f"{i} works")
        print(pow(10, x, i))

#naive
for i in range(desired, desired + 171):
    if i % 2 == 0 or i % 5 == 0:
        continue 
    works = True 
    for j in range(1, desired + 1):
        if pow(10, j, i) == 1:
            works = False
            break
    if works:
        print(i)