logins_file = open("p079_keylog.txt", "r")
logins = []
for i in range(50):
    file_string = logins_file.readline()[:3]
    logins.append(file_string)

left_lists = []
right_lists = []
for i in range(10):
    left_lists.append(set())
    right_lists.append(set())

for login in logins:
    for i in range(3):
        left_string = login[:i]
        right_string = login[i+1:]
        num = int(login[i])
        for c in left_string:
            left_lists[num].add(c)
        for c in right_string:
            right_lists[num].add(c)

print(left_lists)
print(right_lists)

