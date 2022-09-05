limit = 10 ** 9
def reverse(n):
    out = 0
    while(n > 0):
        out *= 10
        out += n%10
        n //= 10
    return out
def has_even_digit(n):
    while n > 0:
        digit = n % 10
        if digit & 1 == 0:
            return True
        n //= 10
    return False
count = 0
for i in range(10,limit):
    if i % 1000000 == 0:
        print(i)
    if i % 10 != 0:
        x = i + reverse(i)
        if not has_even_digit(x):
            count += 1
print(count)