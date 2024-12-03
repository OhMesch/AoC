import re

def generateSolution(filename):
    with open(filename) as f:
        raw = f.read()
    
    multLines = re.findall(r"mul\((\d+),(\d+)\)", raw)
    return sum([int(p[0])*int(p[1]) for p in multLines])
    
if __name__ == "__main__":
    print(generateSolution("ab.dat"))