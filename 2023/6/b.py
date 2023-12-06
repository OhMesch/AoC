import a

import re


def generateSolution(filename):
    with open(filename) as f:
        lines = [l.strip() for l in f.readlines()]
    
    time = int("".join(re.findall(r"\d+", lines[0])))
    record = int("".join(re.findall(r"\d+", lines[1])))

    return a.count_solutions(time,record)
    
if __name__ == "__main__":
    print(generateSolution("ab.dat"))