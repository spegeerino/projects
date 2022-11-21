import math as m
import functions as f
#first 10^4 + 25 done naively
smallprimes = f.prime_list(10**4 + 15)
with open("primes.txt", "w") as primes_file:
    primes_file.write(str(smallprimes))
with open("primes.txt","r") as primes_file:
    global primestring
    global file_list
    global primes_list  
    primestring = primes_file.read()
    file_list = primestring[1:-1].split(",")
    primes_list = [int(i.strip()) for i in file_list]

out = list(primes_list)
lower = 10 ** 4 + 10
upper = 10 ** 8
for i in range(lower + 1, upper, 2):
    if i % 10 ** 5 == 1:
        print(i)
    ok = True
    for p in primes_list:
        if p > lower:
            break
        if i % p == 0:
            ok = False
            break
    if ok:
        out.append(i)

with open("primes.txt", "w") as primes_file:
    primes_file.write(str(out))
