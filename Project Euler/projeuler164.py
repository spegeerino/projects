#recurrence relation, need to keep track of last 2 digits individually 
#matrix?
#we want sum_mn=0^9 a_mn(20)
#last 3 digits sum to <=9, 20 digits long
#start with 3 digit numbers summing to <=9?
#pick 3 numbers that sum to <=8, n > 0
#pick 4 numbers sum to 8
#stars and bars, (8+4-1 choose 8) = 11*5*3 = 165
nums = [[]]
for i in range(10):
    nums[0].append([])
    for j in range(10):
        nums[0][i].append(0)
#nums[length-3][second_last_index][last_index] = number of numbers of length n with second last digit (second_last_index) 
# and last digit (last_index) such that sum of last three digits <= 9
# NAIVE APPROACH FOR TESTING
# naive_count = 0
# for i in range(10000, 100000):
#     last_digit_index = i % 10
#     second_last_index = (i//10) % 10
#     works = True 
#     for pos in range(0,3):
#         if sum([int(d) for d in str(i)[pos:pos+3]]) > 9:
#             works = False
#             break
#     if works:
#         naive_count += 1
#         print(i)
# print(naive_count)
# generate for length of 3
for i in range(100, 1000):
    last_digit_index = i % 10
    second_last_index = (i//10) % 10
    if sum([int(j) for j in str(i)]) <= 9:
        nums[0][second_last_index][last_digit_index] += 1
# create list for length of n+1
desired_length = 20
while len(nums) <= desired_length - 3:
    curr = nums[-1]
    new_len = []
    for i in range(10):
        new_len.append([])
        for j in range(10):
            new_len[i].append(0)
    for sl in range(10):
        for l in range(10 - sl):
            for new in range(10 - sl - l):
                new_len[l][new] += curr[sl][l]
    nums.append(new_len)

res = sum([nums[-1][i][j] for i in range(10) for j in range(10)])
print(res)