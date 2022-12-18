def sol(n):
    l = 2 ** n
    def helper(s, substrs):
        # returns sum of all valid binary circles starting with prefix s
        # going to start shifted over by 1 ccw because we know bordering n 0s is 1 on either side
        if (len(s) == l):
            for i in range(n-1):
                to_add = []
                for j in range(n):
                    to_add.insert(0, s[i-j])
                if to_add in substrs:
                    return 0
                substrs.append(to_add)
            # print(s, substrs)
            return shifted_value(s)
        last_n = s[-(n-1):]
        out = 0
        if (last_n + [0]) not in substrs:
            new_substrs = list(substrs)
            new_substrs.append(last_n + [0])
            out += helper(s + [0], new_substrs)
        if (last_n + [1]) not in substrs:
            new_substrs = list(substrs)
            new_substrs.append(last_n + [1])
            out += helper(s + [1], new_substrs)
        return out 
    
    starter = [1] + ([0] * n) + [1]
    substrings = [[1] + [0] * (n-1), [0] * n, [0] * (n-1) + [1]]
    return helper(starter, substrings)

def shifted_value(s):
    s = s[1:]
    s.append(1)
    out = 0
    p = 1
    for i in range(len(s)):
        out += p * s[len(s) - 1 - i]
        p *= 2
    return out 

def check_equal(l1, l2):
    for i in range(len(l1)):
        if l1[i] != l2[i]:
            return False
    return True 

print(sol(5))
