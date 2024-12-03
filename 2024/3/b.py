import re

def generateSolution(filename):
    with open(filename) as f:
        raw = f.read()
    
    removedDonts = re.sub(r"don't\(\).*?(do\(\)|$)", "", raw)
    with open("temp.txt","w") as f:
        f.write(removedDonts)
    multLines = re.findall(r"mul\((\d+),(\d+)\)", removedDonts)
    return sum([int(p[0])*int(p[1]) for p in multLines])
    
if __name__ == "__main__":
    print(generateSolution("ab.dat"))