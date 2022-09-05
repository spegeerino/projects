from math import sqrt
count = 0
limit = 10**9
#apparently pell's is faster somehow but idk how work
def is_square(n):
    x = sqrt(n)
    return int(x+0.5) ** 2 == n
def has_integral_area(i):
    #sqrt(s(s-i)(s-i)(s-j)) = j/2(sqrt(s(s-j))) = j/2 * sqrt((i+j/2)(i-j/2)) => j is even => i is odd 
    #therefore only req cond is that (i+j/2)(i-j/2) is square => (3i-1)(i+1)/4 is square or (3i+1)(i-1)/4 is square
    # which basically means (3i-1)(i+1) is square or (3i+1)(i-1) is square ==> 3i^2 + 2i - 1 and 3i^2 - 2i - 1 
    # two squares separated by 4i, but the squares are greater than i therefore they cannot both be square
    if is_square((3*i+1)*(i-1)):
        print(str(i) + "," + str(i+1))
        return 3*i + 1
    if is_square((3*i-1)*(i+1)):
        print(str(i) + "," + str(i-1))
        return 3*i - 1
    return 0
for i in range(3,limit//3 + 2,2):
    if i % 1000000 == 1:
        print(i)
    count += has_integral_area(i)

print(count)