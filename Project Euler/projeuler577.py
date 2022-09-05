# this can be solved in O(1) using finite differences, wait no there are weird amounts of 0s for every sequence, so it doesn't work 
# there are two possible orientations of hexagons: two horizontal sides or two vertical sides (so this was wrong)
# horizontal sides fits in a 3x3 triangle, vertical sides fits in a 6x6 triangle
# then we can scale each up so that we get 3x3, 6x6, 9x9, ..., 3nx3n for horizontal sides
# and equivalently 6nx6n for vertical sides
# supposing we have an nxn triangle, then we know that there are (n-k+1)(n-k+2)/2 kxk triangles in the nxn triangle.
import functions as f
limit = 20
total = 0 
for i in range(3, limit + 1):
    prev = total
    for k in range(3, i+1, 3):
        x = f.figurate(i-k+1)
        y = f.num_factors(k//3)
        total += x*y
    print(i, total - prev)
print(total)

def H(n):
    
        
