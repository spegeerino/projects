import functions as f
from timeit import default_timer as dt 
start = dt()
myprimes = [[[2]],[],[],[],[]]
simple_primes = [2]
def concatenate_prime_check(prime_list):
    #can improve by realizing we already checked a lot of these
    for i in range(len(prime_list)):
        for j in range(len(prime_list)):
            if j != i:
                icj = int(str(prime_list[i]) + str(prime_list[j]))
                if not f.is_prime(icj):
                    return False
    return True

def better_cpc(prime_list, new_p):
    #last
    for i in prime_list:
        icnew = int(str(i) + str(new_p))
        newci = int(str(new_p) + str(i))
        if not f.is_prime(icnew) or not f.is_prime(newci):
            return False
    return True 

#suppose we create lists of concatenatable groups of primes and then test adding the next prime to each group 
# and then seeing if that group is valid to be increased.
#this would help a lot i think compared to the most naive method possible

for _ in range(1500):
    if(_ % 100 == 0):
        print(_)
    x = f.next_prime(simple_primes)
    for row_index in range(len(myprimes) - 1):
        for i in range(len(myprimes[row_index])):
            if better_cpc(myprimes[row_index][i], x):
                longer_list = list(myprimes[row_index][i])
                longer_list.append(x)
                myprimes[row_index + 1].append(longer_list)
    myprimes[0].append([x])
    simple_primes.append(x)
    if len(myprimes[4]) != 0:
        break
#cleaner code is not faster code :(
print(myprimes[4])
f.print_time_taken(start, dt())

# done = False
# for counter in range(10000):
#     if counter % 100 == 0:
#         print(counter)
#     prime_subset = [0,0,0,0,0]
#     prime_subset[0] = myprimes[0][-1]
#     for x2 in range(len(myprimes) - 1):
#         prime_subset[1] = myprimes[0][x2]
#         if not concatenate_prime_check(prime_subset[0:2]):
#             continue
#         if done:
#             break
#         for x3 in range(x2):
#             prime_subset[2] = myprimes[0][x3]
#             if not concatenate_prime_check(prime_subset[0:3]):
#                 continue
#             if done:
#                 break
#             for x4 in range(x3):
#                 prime_subset[3] = myprimes[0][x4]
#                 if not concatenate_prime_check(prime_subset[0:4]):
#                     continue
#                 if done:
#                     break
#                 for x5 in range(x4):
#                     prime_subset[4] = myprimes[0][x5]
#                     if not concatenate_prime_check(prime_subset):
#                         continue
#                     else:
#                         print(prime_subset)
#                         done = True
#                     if done:
#                         break
#     if done:
#         break
#     myprimes.append(f.next_prime(myprimes))
print("finished")