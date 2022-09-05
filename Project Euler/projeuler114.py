import functions as f
# So uh yeah this doesn't work 
# -----------------------------------------------------------------------
# #2d array: (length x, ending in y grays)
# #entry x,y = (x-1, y-1) + 2(x-2, 3) + 3(x-3, 4) ... until x < 0 or y > x
# nums = [[1],[0,1],[0,0,1],[1,0,0,1]] 
# #nums[4] = [2,1,0,0,1] which are 4, 13, 31, 1111 --> ok. we make 31 from 3 and 1111 from 111. 
# #we must do further analysis on the [1111] case, (consider adding 1 to both 0 and 1), then for 11111 we add 1 to 0,1,2
# #then for nums[5] we get (5,41,14,311,131,113,11111) 7 total:
# #we group as follows: (41,131,311,11111) gotten by adding 1 to each element of nums[4]
# #then we get 5, 14, and 113 by considering (11111)
# #we must consider any element ending in 3 or more 1s 1s, because when we add our 4th 1 we introduce the possibility of changing again
# for i in range(4, 8):
#     nextrow = f.list_copy(nums[i-1])
#     nextrow.insert(0,i-2)
#     for j in range(3,len(nums[i-1])):
#         if nums[i-1][j] > 0:
#             print((i,j))
#             nextrow[0] += 1
#     print(nextrow)
#     nums.append(nextrow)
# print(sum(nums[7]))
#-----------------------------------------------------------------------
# new idea: recurrence relations with states
# a_n = number of permutations of length n ending in gray square
# b_n = number of permutations of length n ending in red block 
# going to have to store both of these as lists
# how to store 0? probably as ending with gray because we don't want to restrict what we can add to it
# then a_n = a_{n-1} + b_{n-1}
# and b_n = sum from i = 0 to n-3 of a_i
# wonder if can be condensed into one recurrence relation
# a_n + b_n = a_{n-1} + b_{n-1} + [a_i for i in range(0, n-2)] 
# def c_n = a_n + b_n, then c_n = c_{n-1} + [c_i for i in range(-1, n-3)] = 2c_{n-1} - c_{n-2} + c_{n-4}
# nice so there is a single recurrence relation, which means no states necessary
limit = 50
a = [1, 1, 1]
b = [0, 0, 0]
for i in range(3, limit + 1):
    a_i = a[-1] + b[-1]
    b_i = 0
    for j in range(0, i-2):
        b_i += a[j]
    a.append(a_i)
    b.append(b_i)
print(a[50] + b[50])
