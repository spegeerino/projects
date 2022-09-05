with open("primes.txt", "r") as primes_file:
    global primes_list
    primestring = primes_file.read()
    file_list = primestring[1:-1].split(",")
    primes_list = [int(i.strip()) for i in file_list]

print("primes read")
with open("primes.txt", "w") as primes_file:
    for p in primes_list:
        primes_file.write(str(p) + "\n")

print("done")
