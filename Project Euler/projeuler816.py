from math import sqrt 
MOD = 50515093
def P(N):
    x = 290797
    mod = MOD
    y = (x * x) % mod
    yield (x,y)
    for _ in range(1, N):
        x = (y*y) % mod
        y = (x*x) % mod
        yield (x,y)

def dist_sq(a, b):
    return (b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2

def dist(a,b):
    return sqrt(dist_sq(a,b))

def sol(N):
    xs = [i for i in P(N)]
    ys = list(xs)
    print("done generating")
    xs = sorted(xs, key= lambda x: x[0])
    ys = sorted(ys, key= lambda x: x[1])
    print("done sorting")
    smallest = dist_sq((0,0), (MOD, MOD))
    for m in range(len(xs)):
        # m is for middle
        i = m + 1
        while i < len(xs) and (xs[i][0] - xs[m][0]) ** 2 < smallest:
            d = dist_sq(xs[m], xs[i])
            if d < smallest:
                smallest = d
            i += 1
        i = m - 1
        while i >= 0 and (xs[i][0] - xs[m][0]) ** 2 < smallest:
            d = dist_sq(xs[m], xs[i])
            if d < smallest:
                smallest = d
            i -= 1
    print("done with x")
    return sqrt(smallest)

print(f"ans = {round(sol(2000000), 9)}")