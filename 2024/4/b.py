def generateSolution(filename):
    with open(filename) as f:
        lines = f.readlines()
    
    maxH = len(lines)
    maxW = len(lines[0].strip())
    sum = 0
    for y in range(1,maxH-1):
        for x in range(1,maxW-1):
            if lines[y][x] == "A":
                diag1 = lines[y-1][x-1] + lines[y][x] + lines[y+1][x+1]
                diag2 = lines[y-1][x+1] + lines[y][x] + lines[y+1][x-1]
                if diag1 in ['MAS', "SAM"] and diag2 in ['MAS', "SAM"]:
                    sum += 1

    return sum

if __name__ == "__main__":
    print(generateSolution("ab.dat"))