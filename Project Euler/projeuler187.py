with open("primes.txt","r") as primes_file:
    global primes
    primestring = primes_file.read()
    file_list = primestring[1:-1].split(",")
    primes = [int(i.strip()) for i in file_list]

print("primes are loaded")
limit = 10**8
count = 0 
for p1 in primes:
    if p1 % 100000 == 1:
        print(p1)
    for p2 in primes:
        if p2 > p1:
            break
        if p1*p2 > limit:
            break
        else:
            count += 1
print(count)