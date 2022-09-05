#primes asymptotic to nlogn, so 10001st prime appears at about 4*2.3*10001 << 5 * 10^5
import functions as f
primes = f.prime_list(5 * 10**5)
print(primes[10000])