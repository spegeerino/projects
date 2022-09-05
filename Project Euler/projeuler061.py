from functions import figurate

def list_copy(a):
    out = []
    for x in a:
        out.append(x)
    return out

four_digit_figurates = []
for i in range(3,9):
    four_digit_figurates.append([])
for i in range(141):
    x = i+1
    for j in range(3, 9):
        num = figurate(x,j)
        if(len(str(num)) == 4):
            four_digit_figurates[j-3].append(num)

# print(four_digit_figurates)
#create candidates based on starting seed from triangle numbers
#we can WLOG assume that the first number is a triangle number to minimize case checking
pseudo_cycles = []
for tn in four_digit_figurates[0]:
    six_list = [tn]
    candidates = [six_list]
    for iters in range(5):
        new_candidates = []
        for c in candidates:
            for i in range(1,6):
                for fig in four_digit_figurates[i]:
                    if str(c[-1])[2:] == str(fig)[:2] and fig not in c:
                        if iters != 4 or str(c[0])[:2] == str(fig)[2:]:
                            new_candidates.append(list_copy(c))
                            new_candidates[-1].append(fig)
        candidates = list_copy(new_candidates)
    if len(candidates) != 0:
        for element in candidates:
            pseudo_cycles.append(element)

#now check there's one of each figurate type

for x in pseudo_cycles:
    y = list_copy(x)
    figurate_type_set = set()
    for i in range(6):
        for j in range(6):
            if (j not in figurate_type_set) and (y[i] in four_digit_figurates[j]):
                figurate_type_set.add(j)
                break
    if len(figurate_type_set) == 6:
        print(y)
        print(sum(y))
            