# Working from left-to-right if no digit is exceeded by the digit to its left it is called an increasing number; for example, 134468.
# Similarly if no digit is exceeded by the digit to its right it is called a decreasing number; for example, 66420.
# We shall call a positive integer that is neither increasing nor decreasing a "bouncy" number; for example, 155349.
# As n increases, the proportion of bouncy numbers below n increases such that there are only 12951 numbers below one-million that are not bouncy and only 277032 non-bouncy numbers below 10^10.
# How many numbers below a googol (10^100) are not bouncy?

# state-based recurrence relation time 
import functions as f
from functions import print_time_taken as ptt
from timeit import default_timer as dt

def sol(n):
    count = 0
    t_vec_inc = [1] * 10
    t_vec_dec = [1] * 10 
    t_vec_inc[0] = 0
    t_vec_dec[0] = 0
    for _ in range(n - 1):
        count += sum(t_vec_inc) + sum(t_vec_dec) - 9 #-9 to remove double count both inc and dec 
        print(t_vec_inc, t_vec_dec)
        t_new_inc = [0] * 10
        t_new_dec = [0] * 10 
        for k in range(10):
            t_new_inc[k] += sum(t_vec_inc[:k+1])
            t_new_dec[k] += sum(t_vec_dec[k:])
        t_vec_inc = t_new_inc
        t_vec_dec = t_new_dec
    count += sum(t_vec_inc) + sum(t_vec_dec) - 9
    return count

print(sol(100))
        
    
