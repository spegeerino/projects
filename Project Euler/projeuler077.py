import functions as f
#this number is way smaller than i thought it was
upper = 100
primes = f.prime_list_sieve(upper)
nums = []
for i in range(upper):
    nums.append([])
print(len(primes))
for i in primes:
    nums[i].append([i])

for i in range(len(nums)):
    for j in range(len(nums[i])):
        for p in primes:
            if p >= nums[i][j][-1]:
                if i + p >= upper:
                    break
                new_list = f.list_copy(nums[i][j])
                new_list.append(p)
                nums[i+p].append(new_list) 

for i in range(len(nums)):
    if len(nums[i]) > 5000:
        print(i)
        break
print([len(i) for i in nums])