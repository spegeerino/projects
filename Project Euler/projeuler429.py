#need to read primes file, gives primes up to 10^8
primes = []
bigN = 10 ** 8
mod = 1000000009
output = 1

with open("primes.txt", "r") as primes_file:
    s = primes_file.readline()
    while s != "":
        x = int(s)
        if x > bigN:
            break
        primes.append(x)
        s = primes_file.readline()

print("primes read")
for k,i in enumerate(primes):
    if i > bigN:
        break
    x = i
    y = 0
    while x <= bigN:
        y += bigN // x
        x *= i
    factor = pow(i,2*y,mod)
    factor += 1
    output *= factor
    output %= mod
    if k % 100000 == 0:
        print(k,i)
        print(y)
print(output)