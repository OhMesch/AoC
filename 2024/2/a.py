def generateSolution(filename):
    lines = []
    with open(filename) as f:
        for line in f:
            lines.append(list(map(int, line.split())))
    
    diffs = [[line[i]-line[i-1] for i in range(1, len(line))] for line in lines]
    safe = 0
    for diff in diffs:
        if all(x in [-3, -2, -1] for x in diff) or all(x in [1, 2, 3] for x in diff):
            safe += 1
    return safe
        
if __name__ == "__main__":
    print(generateSolution("ab.dat"))