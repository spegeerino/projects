import functions as f
limit = 20
num = 1
for i in range(1, limit + 1):
    num = num * i // f.gcd2(num, i) #lcm of the first i numbers, up to limit of 20
print(num)