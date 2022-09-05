from functions import binom 
def sum_squares(n): #can prove this formula however you want, probably easiest way is finite difference method
    return n*(n+1)*(2*n+1)//6

def square_sum(n):
    return binom(n+1, 2)**2 #sum of natural numbers is (n+1)n/2, then you just square it 

print(square_sum(100) - sum_squares(100))