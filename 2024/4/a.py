import re

def generateSolution(filename):
    with open(filename) as f:
        lines = f.readlines()
    
    maxH = len(lines)
    maxW = len(lines[0].strip())
    charString = [c for line in lines for c in line.strip()]

    vertStr = [charString[i*maxW:(i+1)*maxW] for i in range(maxW)]
    hortStr = [charString[i::maxW] for i in range(maxH)]
    diagXStr = [charString[i::maxW+1][:maxW-i] for i in range(maxW)]
    antiXStr = [charString[i::maxW-1][:i+1] for i in range(maxW)]
    diagYStr = [charString[i*maxW::maxW+1] for i in range(1,maxH)]
    antiYStr = [charString[i*maxW+maxW-1::maxW-1][:maxH-1] for i in range(1,maxH)]

    forwardStrings = vertStr + hortStr + diagXStr + diagYStr + antiXStr + antiYStr
    reverseStrings = [list(reversed(s)) for s in forwardStrings]
    allStrings = ["".join(sArr) for sArr in forwardStrings + reverseStrings if len(sArr) > 3]

    return sum([len(re.findall(r"XMAS", s)) for s in allStrings])

if __name__ == "__main__":
    print(generateSolution("ab.dat"))