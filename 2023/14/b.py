from collections import deque
import numpy as np

def parseInputFile(filename):
    with open(filename, "r") as f:
        return [[c for c in l.strip()] for l in f.readlines()]

def shiftUp(rock_grid):
    shifted_rock_grid = rock_grid.copy()

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
                    shifted_rock_grid[shift_idx.popleft()][x] = "O"
                    shifted_rock_grid[y][x] = "."
                    shift_idx.append(y)
    return shifted_rock_grid

def spin(rock_grid):
    rock_grid = shiftUp(rock_grid)
    for _ in range(3):
        rock_grid = np.rot90(rock_grid, k=-1)
        rock_grid = shiftUp(rock_grid)
    rock_grid = np.rot90(rock_grid, k=-1)

    return rock_grid

def calculateNorthLoad(rock_grid):
    load = 0
    load_at_y = lambda y: len(rock_grid) - y
    for y_idx, y in enumerate(rock_grid):
        load += sum([load_at_y(y_idx) for x in y if x == "O"])

    return load

def generateSolution(filename):    
    rock_grid = parseInputFile(filename)

    grid2string = lambda grid: "\n".join(["".join(x) for x in grid])
    seen = dict()
    
    curr_cycle = 0
    target_cycles = 1000000000
    while (target_cycles):
        spun_grid = spin(rock_grid)

        spun_grid_string = grid2string(spun_grid)
        if spun_grid_string in seen:
            loop_size = curr_cycle - seen[spun_grid_string]
            remaining_cycles = target_cycles - curr_cycle
            idx_at_completion = remaining_cycles % loop_size
            target_cycles = curr_cycle + idx_at_completion
            break
        seen[spun_grid_string] = curr_cycle

        rock_grid = spun_grid
        curr_cycle += 1
        target_cycles -= 1

    for _ in range(target_cycles):
        rock_grid = spin(rock_grid)

    return calculateNorthLoad(rock_grid)
    
if __name__ == "__main__":
    print(generateSolution("ab.dat"))