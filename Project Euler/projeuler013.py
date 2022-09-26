# python can handle integers of arbitary size but going to implement BigInteger class anyway
class big_integer:
    def __init__(self, s: str) -> None:
        self.digits = []
        for c in s:
            x = int(c)
            self.digits.append(x)
    
    def length(self) -> int:
        return len(self.digits)
    
    def print_digits(self):
        print(self.digits)
    
    def __add__(self, other):
        new_digits = [0] * max(self.length(), other.length())
        for i in range(self.length()):
            index = len(new_digits) - self.length() + i
            new_digits[index] += self.digits[i]
        for i in range(other.length()):
            index = len(new_digits) - other.length() + i
            new_digits[index] += other.digits[i]
        for i in range(len(new_digits) - 1, 0, -1):
            if new_digits[i] >= 10:
                new_digits[i] -= 10
                new_digits[i-1] += 1
        if new_digits[0] >= 10:
            new_digits.insert(0, 1)
            new_digits[1] -= 10
        return big_integer("".join([str(c) for c in new_digits]))
    
    def __str__(self):
        return "".join([str(x) for x in self.digits])

def main():
    with open("p013_nums.txt", "r") as file:
        global nums
        nums = []
        file_str = file.readline()
        while file_str:
            nums.append(big_integer(file_str.strip()))
            file_str = file.readline()

    total = big_integer("0")
    for n in nums:
        total += n
    print(str(total)[:10]) #first 10 digits

if __name__ == "__main__":
    main()