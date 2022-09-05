from numpy import Inf, Infinity
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
#dijkstra's
def find_minimal_path(mat):
    assert len(mat) == len(mat[0]), "matrix is not square"
    known_distance_arr = []
    known_distance_dict = {}
    for _ in range(len(mat)):
        new_row = [Infinity] * len(mat)
        known_distance_arr.append(new_row)
    known_distance_arr[-1][-1] = mat[-1][-1]
    steps = 0
    while len(known_distance_dict.keys()) <= len(mat)**2 and steps <= len(mat)**2:
        steps += 1
        data = find_smallest_val(known_distance_arr, known_distance_dict.keys())
        x,y = data[0]
        known_distance_dict[data[0]] = data[1]
        known_vertices = known_distance_dict.keys()
        #left 
        update_neighbor(mat, known_distance_arr, known_vertices, x-1, y, data[1])
        #up
        update_neighbor(mat, known_distance_arr, known_vertices, x, y-1, data[1])
        #right remove for 3 and 2
        update_neighbor(mat, known_distance_arr, known_vertices, x+1, y, data[1])
        #down remove for 2
        update_neighbor(mat, known_distance_arr, known_vertices, x, y+1, data[1])
    return known_distance_dict[(0,0)]
        
def update_neighbor(mat, kda, kv, x, y, path_l):
    if x in range(len(kda)) and y in range(len(kda)) and (x,y) not in kv:
        xy_path = path_l + mat[x][y]
        if xy_path < kda[x][y]:
            kda[x][y] = xy_path

def find_smallest_val(mat, excluded = []):
    pos = (-1,-1)
    smallest = Infinity
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if (i,j) not in excluded and mat[i][j] < smallest:
                pos = (i,j)
                smallest = mat[i][j]
    return pos, smallest

print(find_minimal_path(smallmatrix))
print(find_minimal_path(bigmatrix))