perms = {}
master_sorted_strings = []
for i in range(1,10000):
    n = i**3
    digits = [c for c in str(n)]
    digits.sort()
    sorted_string = "".join(digits)
    if sorted_string not in perms.keys():
        perms[sorted_string] = 0
    perms[sorted_string] += 1
    if perms[sorted_string] == 5:
        print(sorted_string)
        master_sorted_strings.append(sorted_string)

for i in range(1,10000):
    n = i**3
    digits = [c for c in str(n)]
    digits.sort()
    sorted_string = "".join(digits)
    if sorted_string in master_sorted_strings:
        print(i)
        print(n)
        break