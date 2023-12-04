import re

gear_adjacencies = {}

def addAdj2GearDict(schematic, i, j_range):
    seen = set()
    value = int(schematic[i][j_range[0]:j_range[1]])

    def addLocIfNew(i, j):
        key = f"({i}, {j})"
        if key not in seen:
            seen.add(key)
            if key in gear_adjacencies:
                gear_adjacencies[key].append(value)
            else:
                gear_adjacencies[key] = [value]

    if j_range[0] > 0:
        if schematic[i][j_range[0]-1] == "*":
            addLocIfNew(i, j_range[0]-1)
    
    if j_range[1] < len(schematic[i]):
        if schematic[i][j_range[1]] == "*":
            addLocIfNew(i, j_range[1])
    
    j_start = max(j_range[0] - 1, 0)
    j_end = min(j_range[1] + 1, len(schematic[i]))

    if i > 0:
        for j in range(j_start, j_end):
            if schematic[i-1][j] == "*":
                addLocIfNew(i-1, j)
    
    if i < len(schematic)-1:
        for j in range(j_start, j_end):
            if schematic[i+1][j] == "*":
                addLocIfNew(i+1, j)

    return False

def generateSolution(filename):
    schematic = []
    for line in open(filename):
        schematic.append(line.strip())
    
    running_sum = 0
    for i, line in enumerate(schematic):
        for m in re.finditer(r"(\d+)", line):
            addAdj2GearDict(schematic, i, m.span())
    
    for _, adjs in gear_adjacencies.items():
        if len(adjs) == 2:
            running_sum += adjs[0]*adjs[1]

    return running_sum
    
if __name__ == "__main__":
    print(generateSolution("ab.dat"))