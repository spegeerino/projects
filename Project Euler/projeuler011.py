with open("p011_matrix.txt", "r") as f:
    global matrix
    matrix = []
    curr_line = f.readline()
    while curr_line:
        row = curr_line.split()
        row = [int(i) for i in row]
        matrix.append(row)
        curr_line = f.readline()

def four_product(i, j, iv, jv):
    out = matrix[i][j]
    for x in range(1,4):
        out *= matrix[i + iv*x][j + jv*x]
    return out
#horizontal
max_product = -1
for i in range(len(matrix)):
    for j in range(len(matrix)-3):
        max_product = max(four_product(i, j, 0, 1), max_product)

#vertical
for i in range(len(matrix) - 3):
    for j in range(len(matrix)):
        max_product = max(four_product(i, j, 1, 0), max_product)

#-slope diagonal
for i in range(len(matrix) - 3):
    for j in range(len(matrix) - 3):
        max_product = max(four_product(i, j, 1, 1), max_product)

#+ slope diagonal
for i in range(3, len(matrix)):
    for j in range(len(matrix) - 3):
        max_product = max(four_product(i, j, -1, 1), max_product)

print(max_product)