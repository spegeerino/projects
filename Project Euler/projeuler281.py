#f(m,n) = mn! / (mn)*(n!)^m --> mn! possible colorings, divide by mn to elim rotations (this is wrong), and (n!)^m covers permutations of identical slices
#upper bound on m or n?, remember that f(m,n) < 10^15
#for fixed m, f(m,n) is minimized at n = 1
#f(19, 1) = 18! > 10^15
# so 2 <= m <= 18
# then we need to just check until n is too large and then we're done
# now, what if there are less than mn rotations, we can have md rotations for any divisor d of n 
# for fixed d, there are (md-1)! / ()
import functions as f 
def func(m,n):
    out = f.factorial(m*n-1)
    out //= pow(f.factorial(n), m) 
    return out 
print(func(3,2))
