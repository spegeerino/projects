#hamming numbers of type 100
#numbers with all prime factors < 100
import functions as f
primes = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]
limit = 10 ** 9
pf = {}
count = 0
for i in primes:
    pf[i] = 0
while True:
    overflow = False
    i = 0
    x = f.pf_eval(pf) #returns product of primes in pf 
    while x > limit:
        overflow = True
        x //= primes[i] ** pf[primes[i]]
        pf[primes[i]] = 0
        i += 1
    if i == 25: #number of primes less than 100, this is curr index of prime to increase in primes list
        break
    if overflow:
        pf[primes[i]] += 1
    else:
        count += 1
        if count % 100000 == 0:
            print(count)
        pf[primes[0]] += 1
print("------")
print(count)

            
