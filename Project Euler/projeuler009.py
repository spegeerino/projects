#pythagorean triples generated by squaring complex numbers
#suppose you have z = m + ni
#then |z| = sqrt(m^2+n^2) which is the sqrt of an integer
#so |z^2| = sqrt(m^2+n^2)^2 is an integer, which means we have a right triangle with integer sides
#the legs are given by real and imaginary part of z^2 and the hypotenuse is the magnitude
#z^2 = (m^2-n^2) + (2mn)i
#therefore we want two integers m,n such that m>n and (m^2-n^2) + (2mn) + (m^2 + n^2) = 1000, and then we want to calculate this product
#we simplify: 2m(m+n) = 1000, m(m+n) = 500
#we need a factor pair ab = 500 with a < b < 2a, we can see 20*25, so m = 20 and n = 5
#then we simply calculate the product
m = 20
n = 5
out = (m*m-n*n) * (2*m*n) * (m*m + n*n)
print(out)