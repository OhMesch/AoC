import re
import string

def adjacent2Symbol(schematic, i, j_range):
    if j_range[0] > 0:
        if schematic[i][j_range[0]-1] not in string.digits+".":
            return True
    
    if j_range[1] < len(schematic[i]):
        if schematic[i][j_range[1]] not in string.digits+".":
            return True
    
    j_start = max(j_range[0] - 1, 0)
    j_end = min(j_range[1] + 1, len(schematic[i]))

    if i > 0:
        for j in range(j_start, j_end):
            if schematic[i-1][j] not in string.digits+".":
                return True
    
    if i < len(schematic)-1:
        for j in range(j_start, j_end):
            if schematic[i+1][j] not in string.digits+".":
                return True

    return False

def generateSolution(filename):
    schematic = []
    for line in open(filename):
        schematic.append(line.strip())
    
    running_sum = 0
    for i, line in enumerate(schematic):
        for m in re.finditer(r"(\d+)", line):
            if adjacent2Symbol(schematic, i, m.span()):
                running_sum += int(m.group(1))
    
    return running_sum
    
if __name__ == "__main__":
    print(generateSolution("ab.dat"))