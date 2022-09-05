#hyper exponent: 1777 ^^^ 1855 mod 10^8 means 1777^1777^1777.... 1855 times
#subsequent totients of 10^8: 
#2^8 * 5^8
#2^9 * 5^7
#2^10 * 5^6
#2^11 * 5^5
#2^12 * 5^4
#2^13 * 5^3
#2^14 * 5^2
#2^15 * 5
#2^16 --> 2
#consider mod 10 first:
#1777^1777^1777 mod 10 means i need to consider 1777^1777 mod 4 means i need to consider 1777 mod 2 which is 1, so then i have 1777 mod 4 which is 1, then i have 1777 mod 10 which is 7
#1777 mod 8 is 1
#1777 mod 16 is 1
#1777 mod 32 is 17
#1777^17 mod 64 is 
totients = []
for i in range(1, 17):
    totients.append(1 << i)
for i in range(1, 9):
    totients.append((5**i) << 16-i)
x = 1
num = 1777
print(totients)
for t in totients:
    x = pow(num, x, t)
print(x)