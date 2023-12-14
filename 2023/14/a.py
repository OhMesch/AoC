from collections import deque

def parseInputFile(filename):
    with open(filename, "r") as f:
        return [[c for c in l.strip()] for l in f.readlines()]

def shiftUpAndCalculateLoad(rock_grid):
    load = 0
    load_at_idx = lambda y: len(rock_grid) - y

    shift_idx = deque()
    for x in range(len(rock_grid[0])):
        shift_idx.clear()
        for y in range(len(rock_grid)):
            if rock_grid[y][x] == ".":
                shift_idx.append(y)
            elif rock_grid[y][x] == "#":
                shift_idx.clear()
            else:
                if len(shift_idx):
                    shifts_to = shift_idx.popleft()
                    shift_idx.append(y)
                else:
                    shifts_to = y
                load += load_at_idx(shifts_to)
    return load

def generateSolution(filename):
    rock_grid = parseInputFile(filename)

    return shiftUpAndCalculateLoad(rock_grid)
    
if __name__ == "__main__":
    print(generateSolution("ab.dat"))