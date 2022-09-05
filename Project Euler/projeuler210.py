# Consider the set S(r) of points (x,y) with integer coordinates satisfying |x| + |y| ≤ r.
# Let O be the point (0,0) and C the point (r/4,r/4).
# Let N(r) be the number of points B in S(r), so that the triangle OBC has an obtuse angle, i.e. the largest angle α satisfies 90°<α<180°.
# So, for example, N(4)=24 and N(8)=100.
# What is N(1,000,000,000)?

#we have that x + y < 0 or x + y > r/2 = (10 ** 9 / 2) or (x - r/8)^2 + (y - r/8)^2 < (r/8)^2
#first two can be counted easily:
#first one = r/2(r), second one is r/4(r), sum is 3r^2/4
#function based on even r
#circle condition is like, we can count most of the points rudimentarily and then iterate over remaining ones
#or we can just count squares summing to something, multiply by 4, (as long as x - y =/= 0)
#circle has radius r/8, (we can center at 0 to make counting easier)
#square of side rsqrt(2)/8 contains only lattice points we want (except for 4 of them)
#excluding ones where x = y, which we can count easily
LIMIT = 10 ** 9
def N(r):
    extra_points = r//4 - 1
    return 3*r*r//2 #+ circle stuff

print(N(4))