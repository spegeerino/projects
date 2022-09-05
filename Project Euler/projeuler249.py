import functions as f
from timeit import default_timer as dt
from functions import print_time_taken as ptt 
upper_prime = 2501 * 2500
primes = f.prime_list(upper_prime)
gen_poly = [0] * (upper_prime + 1) # this is too slow isn't it 
print(len(primes))