# rotate? probably not helpful (can maybe use to check boundaries)
# x^2 + xy + 41y^2 = AX^2 + BY^2 
# (x + y/2)^2 + 163y^2/4
# X = (xcost + ysint), Y = (ycost - xsint)
# x = (Xcost - Ysint), y = (Ycost + Xsint)
# (Xcost - Ysint)^2 + (Xcost - Ysint)(Xsint + Ycost) + 41(Xsint + Ycost)^2
# X^2cos^2t - 2XYcostsint + Y^2sin^2t + X^2costsint - XYsin^2t - Y^2costsint + XYcos^2t + 41X^2sin^2t + 82XYcostsint + 41Y^2cos^2t
# XY(40sin2t - cos2t) = 0, cos2t = 40sin2t, tan2t = 1/40, sin2t = sqrt(1/1601), cos2t = sqrt(1600/1601)
# X^2 + 40X^2sin^2t, cos 2t = 1 - 2sin^2t, sin^2t = 1-cos2t/2, A = 
# - - - - - - - -  - - - -  - -
# lagrange multipliers: minimize/maximize y while x^2 + xy + 41y^2 <= limit
# minimized when y equals limit because derivative is 1
# if y positive, then minimizing x is -y/2
# if y negative, then minimizing x is -y/2, so we subtract: y^2/4 - y^2/2 + 41y^2 = 163y^2/4 is the min value of the func
# therefore we can optimize around this y
from math import isqrt, sqrt, ceil, floor
import functions as funcs
import timeit 
def simplef(N):
    count = 0
    y_limit = floor(sqrt(4*N/163))
    print(y_limit)
    for y in range(-y_limit, y_limit + 1):
        if y % 200000 == 0:
            print(y)
        #we just have a parabola now, can find intersections with x-axis and easily count number of valid x values
        #look at parabola x^2 + (y)x + (41y^2-limit) = 0, solve for intersections with x-axis, find in between
        b = y
        c = 41*y*y - N
        x1 = ceil((- b - sqrt(b*b - 4*c)) / 2)
        x2 = floor((- b + sqrt(b*b - 4*c)) / 2)
        count += x2 - x1 + 1
    return count - 1 #remove (0,0) because not included 

start = timeit.default_timer()
print(simplef(10**12))
end = timeit.default_timer()
funcs.print_time_taken(start, end)
