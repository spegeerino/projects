#we need right triangles such that:
#(1) primitive (gcd a,b,c = 1)
#(2) hypotenuse is perfect square c = k^2
#(3) area is not multiple of 84 (ab mod 168 != 0)
#a = m^4 - 6m^2n^2 + n^4, b = 4mn(m^2-n^2), c = (m^2 + n^2)^2
#a = (m^2-n^2)^2 - 4m^2n^2 = (m^2-2mn-n^2)(m^2+2mn-n^2)
#should guarantee (2)
# gcd(m,n) = 1 guarantees gcd(a,b) = 1? not sure
# m > n > 0
#LOL THE ANSWER IS 0
#ok find proof now
#ab = 4mn(m^2-2mn-n^2)(m^2+2mn-n^2)(m+n)(m-n)
#ab = 4mn((m+n)^2 -2n^2)((m-n)^2-2n^2)(m+n)(m-n)
#ab = 4mn(m+n)(m-n) covers powers of 2 and 3 necessary
#ab = (m^4- 6m^2n^2 + n^4)(4mn)(m^2-n^2) mod 7 = (m^4 + m^2n^2 + n^4)(m^2 - n^2) = (m^6 - n^6) mod 7 by difference of cubes
#FLT gives m^6 - n^6 mod 7 = m^0 - n^0 mod 7 = 0 as we wanted
#therefore there exist no perfect but not super perfect triangles
count = 0
import numpy as np
limit = 10 ** 16
for m in range(2, 10 ** 4):
    if m % 100 == 0:
        print(m)
        print(count)
    for n in range(1, m):
        if np.gcd(m,n) == 1:
            a = m**4 - 6 * (m*m*n*n) + n**4
            b = 4*m*n*(m*m-n*n)
            c = (m*m+n*n)**2
            if c > limit:
                break
            a %= 168
            b %= 168
            if a*b % 168 != 0:
                count += 1
print(count)
