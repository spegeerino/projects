import functions as f
import timeit 
nums = {}
limit = 10**9
def check(n):
    return n == f.reverse(n)
start = timeit.default_timer()
for i in range(1, 10 ** 3):
    if i % 100 == 0:
        print(i)
    for j in range(1, 40000):
        n = i*i*i + j*j
        if n > limit:
            break
        if not check(n):
            continue
        if n in nums.keys():
            nums[n] += 1
        else:
            nums[n] = 1
nums_list = []
for k in nums.keys():
    if nums[k] == 4:
        nums_list.append(k)
nums_list.sort()
end = timeit.default_timer()
print(nums_list[:5])
print(sum(nums_list[:5]))
print("time taken: " + str(end-start) + "s")