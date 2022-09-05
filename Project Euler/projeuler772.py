import functions as f
with open("primes.txt", "r") as primes_file:
    global primes_list
    primestring = primes_file.read()
    file_list = primestring[1:-1].split(",")
    primes_list = [int(i.strip()) for i in file_list]
print("primes loaded")
mod = 1000000007
num = 10**8
sqrtnum = 10 ** 4
totalnum = 1
for p in primes_list:
    if p % 1 == 10000:
        print(p)
    if p < sqrtnum:
        x = p*p
        while x*p < num:
            x *= p
        totalnum *= x
        totalnum %= mod
    elif p < num:
        totalnum *= p
        totalnum %= mod
    else:
        break

#2*lcm
print((2*totalnum) % mod)