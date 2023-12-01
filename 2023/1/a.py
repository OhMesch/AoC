import re

def generateSolution(filename):
    running_sum = 0
    with open(filename) as f:
        for line in f:
            digit_matches = re.findall(r'(\d)', line)
            running_sum += int(digit_matches[0]+digit_matches[-1])
    return running_sum

if __name__ == "__main__":
    print(generateSolution("ab.dat"))