import functions as f
limit = 10 ** 7
min = 200

def is_perm(a,b):
    if len(str(a)) == len(str(b)):
        a_list = [int(i) for i in str(a)]
        b_list = [int(i) for i in str(b)]
        a_list.sort()
        b_list.sort()
        for i in range(len(a_list)):
            if a_list[i] != b_list[i]:
                return False
        return True
    return False

for i in range(2, limit):
    t = f.totient(i)
    if is_perm(i,t):
        x = i/t
        if x < min:
            min = x
            print(i)

print(min)