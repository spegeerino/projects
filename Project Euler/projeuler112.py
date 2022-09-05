def is_bouncy(n):
    digits = [int(i) for i in str(n)]
    #increasing/decreasing check
    increasing = True
    for i in range(0, len(digits) - 1):
        if digits[i+1] < digits[i]:
            increasing = False
            break
    decreasing = True
    for i in range(0, len(digits) - 1):
        if digits[i+1] > digits[i]:
            decreasing = False
            break
    return (not increasing) and (not decreasing)

count = 0
for i in range(1, 10 ** 8):
    if is_bouncy(i):
        count += 1
    if count / i == 0.99:
        print(i)
        break
    
