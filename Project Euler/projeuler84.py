#it's time for dumb markov chains 
#wait i have a system of 120 equations 
#pain 
from functions import vector_matrix_mul as vmm 
prob_matrix = []
for i in range(120):
    prob_matrix.append([0]*120) 

def edit_col(col, mat, i):
    for j in range(len(mat)):
        mat[j][i] = col[j]


