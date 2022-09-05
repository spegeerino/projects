def game(n):
    count = 1
    outcomes = {}
    outcomes[0] = 0
    outcomes[1] = 0 # player who loses
    outcomes[2] = 1
    for i in range(3,n+1):
        x = 0
        for j in range(i-2):
            x += outcomes[j] + outcomes[i-2-j]
        x %= 2
        outcomes[i] = x
        if x == 1:
            count += 1
    return count

print(game(50))
    

