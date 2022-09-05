import functions as f
limit = 25 * 10 ** 6
# find sols to c^2 - 2a^2 = -1 to allow use of symmetry 
# use pell's 
x = 1
y = 1
valid_ns = [] 
while x <= limit // 2:
    x, y = x + 2 * y, x + y
    x, y = x + 2 * y, x + y
    valid_ns.append(x)
print(valid_ns)
#a^2 + b^2 = c^2 + 1 --> c^2 - b^2 = a^2 - 1 
#(c+b)(c-b) = (a+1)(a-1)
#if i iterate over a and check for num of factor pairs that could work 
#however need b >= a, becomes awkward
for a in range(1, limit // 3 + 1):
