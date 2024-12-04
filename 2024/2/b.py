def generateSolution(filename):
    with open(filename, "r") as f:
        lines = f.readlines()

    lines = [list(map(int, line.split())) for line in lines]

    def isSafe(line):
        diff = [line[i]-line[i-1] for i in range(1, len(line))]
        return all([x in [-3, -2, -1] for x in diff]) or all([x in [1, 2, 3] for x in diff])

    safe = 0
    for line in lines:
        for i in range(len(line)):
            if isSafe(line[:i] + line[i+1:]):
                safe += 1
                break
    return safe

if __name__ == "__main__":
    print(generateSolution("ab.dat"))