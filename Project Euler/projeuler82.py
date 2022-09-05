import functions
def print_matrix(mat):
    for i in range(len(mat)):
        print(mat[i])
f = open("p082_matrix.txt","r")
smallmatrix = [
    [131,673,234,103,18],
    [201,96,342,965,150],
    [630,803,746,422,111],
    [537,699,497,121,956],
    [805,732,524,37,331]
]
bigmatrix = []
exec("bigmatrix = " + f.read())
# idea: find the least expensive path to the end for the second from right col to the rightmost col: 
# then create a new matrix removing the last two columns and replacing with one column that has those path values

def reduce_last_two(mat):
    n_rows = len(mat)
    new_col = []
    for i in range(n_rows):
        #find shortest path from mat[i][-2] to last column
        new_col.append(best_to_last(i,mat))
    for row in mat:
        row.pop()
        row.pop()
    for i in range(n_rows):
        mat[i].append(new_col[i])

def best_to_last(start, mat):
    '''
    start is the column position in the second to last row
    mat is the matrix to traverse
    returns cost of best path
    '''
    #check moving right immediately to establish upper bound
    out = 1 << 31
    #check upwards path
    upwards_path = [mat[start][-2]]
    y_pos = start
    while sum(upwards_path) < out:
        move_right = sum(upwards_path) + mat[y_pos][-1]
        if move_right < out:
            out = move_right
        y_pos -= 1
        if y_pos < 0:
            break 
        upwards_path.append(mat[y_pos][-2])
    #check downwards path
    downwards_path = [mat[start][-2]]
    y_pos = start
    while sum(downwards_path) < out:
        move_right = sum(downwards_path) + mat[y_pos][-1]
        if move_right < out:
            out = move_right
        y_pos += 1
        if y_pos >= len(mat):
            break 
        downwards_path.append(mat[y_pos][-2])
    return out

while len(bigmatrix[0]) >= 2:
    reduce_last_two(bigmatrix)
print(min([x[0] for x in bigmatrix]))
print(bigmatrix)
