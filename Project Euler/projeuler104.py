import functions as f 
def fib(k):
    # returns fk and fk-1
    if k < 3:
        return 1
    x = 1
    y = 1
    for i in range(k-2):
        temp = x
        x = x+y 
        y = temp
    return x,y

def checkpandigital(l):
    return len(set(l)) == 9

def valid(n):
    lastdigits = [int(i) for i in str(n)[-9:]]
    return 0 not in lastdigits and checkpandigital(lastdigits)

x,y = f.fast_fib(2747, 10**9)
x %= 10 ** 9
y %= 10 ** 9
for k in range(2749, 10000000):
    x,y = x+y, x 
    x %= 10 ** 9
    y %= 10 ** 9
    if valid(x):
        print((x,k))
        test = f.fast_fib(k)[1]
        firstdigits = [int(i) for i in str(test)[:9]]
        if 0 not in firstdigits and checkpandigital(firstdigits):
            print(k)
            break 


