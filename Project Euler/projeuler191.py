#iterate over lists with 0 ones and 1 one separately
#recursive formula: six states need a matrix
# a = 0
# l = 1
# o = 2
# a_n = no lates and not ending with an absence
# b_n = 1 late and not ending with an absence
# c_n = no lates and ending with one absence
# d_n = 1 late and ending with one absence
# e_n = no lates and ending with two absences
# f_n = 1 late and ending with two absences
# a_{n+1} = a_n (on time) + c_n (on time) + e_n (on time)
# b_{n+1} = a_n (late) + b_n (on time) + c_n (late) + d_n (on time) + e_n (late) + f_n (on time)
# c_{n+1} = a_n (absence)
# d_{n+1} = b_n (absence)
# e_{n+1} = c_n (absence)
# f_{n+1} = d_n (absence)
# desired output = a_30 + b_30 + c_30 + d_30 + e_30 + f_30 = b_31
# start with empty string: a = 1, rest = 0
# -------------------------
# can maybe improve to single state recurrence relation with algebra
# b_{n+1} = b_n + a_(n+1) + b_{n-1} + b_{n-2}
# a_{n+1} = a_n + a_{n-1} + a_{n-2}, can solve this recurrence relation independently
# r^3 - r^2 - r - 1 = 0, no rational roots so we have to do some cubic stuff 
# (r-k)^3 - (r-k)^2 = r^3 - 3kr^2 - r^2
# r = s + 1/3
# (s + 1/3)^3 - (s+1/3)^2 - (s+1/3) - 1 = 0
# s^3 + s^2 + s/3 + 1/27 - s^2 - 2s/3 - 1/9 - s - 1/3 - 1 = 0
# s^3 - 4s/3 - 38/27 = 0
# 3st = -4/3
# s^3 - t^3 = -38/27
# (-4/9t)^3 - t^3 = -38/27
# t^6 - 38t^3/27 + 64/729 = 0
import functions as f
sol_vec = [1,0,0,0,0,0]
recur_mat = [[1,0,1,0,1,0],
             [1,1,1,1,1,1],
             [1,0,0,0,0,0],
             [0,1,0,0,0,0],
             [0,0,1,0,0,0],
             [0,0,0,1,0,0]]

str_len = 30
for _ in range(str_len):
    sol_vec = f.vector_matrix_mul(sol_vec, recur_mat, 0)
print(sum(sol_vec))
