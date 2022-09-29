num_users = 10 ** 6
users = [-1] * num_users
PM = 524287
size_limit = 99 * num_users // 100

def parent(i):
    while users[i] >= 0:
        i = users[i]
    return i

def is_connected(i,j):
    return parent(i) == parent(j)

def connect(i, j):
    if is_connected(i, j):
        return
    pi = parent(i)
    pj = parent(j)
    if users[pi] < users[pj]:
        users[pi] = users[pi] + users[pj]
        users[pj] = pi
    else:
        users[pj] = users[pi] + users[pj]
        users[pi] = pj

vals = [(100003 - 200003 * k + 300007 * k*k*k) % num_users for k in range(1, 56)]
vals.append(vals[-24] + vals[-55])
print(vals)
i = 0
count = 0
while users[parent(PM)] > -size_limit:
    caller = 0
    called = 0
    if i > 55:
        new_val = (vals[-24] + vals[-55]) % num_users
        vals = vals[1:]
        vals.append(new_val)
        new_val = (vals[-24] + vals[-55]) % num_users
        vals = vals[1:]
        vals.append(new_val)
        caller = vals[-2]
        called = vals[-1]
    else:
        caller = vals[i]
        called = vals[i+1]
    i += 2
    if caller != called:
        count += 1
    if count % 100000 == 0:
        print(count)
    connect(caller, called)
print(count)
