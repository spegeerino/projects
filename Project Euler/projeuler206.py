import functions as f
import math as m
def create_num(digits):
    numstring = ""
    for i in range(1,9):
        numstring += str(i)
        numstring += str(digits[i-1])
    numstring += "9"
    return int(numstring)

def num_to_digits(n):
    n_list = [int(i) for i in str(n)]
    for i in range(8-len(n_list)):
        n_list.insert(0,0)
    return n_list

def main():
    timecheck = 10 ** 6
    for i in range(0,10 ** 8,9):
        if i % timecheck == 0:
            print(i)
        num = create_num(num_to_digits(i))
        if f.is_square(num):
            print(int(m.sqrt(int(str(num) + "00"))))
            break

if __name__ == "__main__":
    main()