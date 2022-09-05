#O(log n), there exists O(log log n) sol but too lazy
even_fib_vec = [2,0]
limit = 4 * 10 ** 6
total = 0
def recur(v):
    return [4*v[0] + v[1] , v[0]]
while even_fib_vec[0] < limit:
    total += even_fib_vec[0]
    even_fib_vec = recur(even_fib_vec)
print(total)