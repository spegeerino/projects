def naive_sol(N):
    count = N
    queue = [(1,1)]
    val = 0
    while len(queue) != 0:
        new_queue = []
        for x,y in queue:
            count += 2 * val * max(x,y)