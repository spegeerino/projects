#prime digit replacements
#have to replace 3n digits at once otherwise can't work
#how to iterate up numbers?
import functions as f
import random as r
test = ['*', '^', '*', '^','*','last']

def run_test(digits):
    possible_last_digits = ['1','3','7','9']
    for d in possible_last_digits:
        digits[-1] = d
        x = number_valid(digits)
        #print(digits)
        #print(x)
        if x == 8:
            print("".join(digits))
            break
    
def number_valid(digits):
    lower = int(digits[0] == '*')
    out = 0
    for i in range(lower, 10):
        test_digits = []
        for d in digits:
            if d == '*':
                test_digits.append(str(i))
            else:
                test_digits.append(d)
        test_num = int("".join(test_digits))
        if test_num % 3 == 0:
            return 0
        out += f.is_prime(test_num)
    return out

def pick_ints_from_range(lower, upper, num = 1):
    out = []
    nums = list(range(lower,upper))
    for i in range(num):
        decider = r.randint(0,len(nums)-1)
        out.append(nums.pop(decider))
    return out

def create_basic_tests(num_digits):
    out = ['^'] * (num_digits - 1)
    for i in pick_ints_from_range(0, len(out),3):
        out[i] = '*'
    out.append('last')
    print(out)

def run_all_basic_test_forms(digits):
    for i in range(len(digits)):
        if digits[i] == '^':
            lower = int(i == 0)
            for j in range(lower, 10):
                digits[i] = str(j)
                if '^' in digits:
                    run_all_basic_test_forms(digits)
                else:
                    run_test(digits)
            digits[i] = '^'
            
run_all_basic_test_forms(test)