import numpy as np

import sys
sys.setrecursionlimit(10000)

def parseInputFile(filename):
    with open(filename, "r") as f:
        return([[c for c in l.strip()] for l in f.readlines()])

def visualize(grid, laser_start):
    print()
    visual = []
    for y in range(len(grid)):
        curr_line = []
        for x in range(len(grid[0])):
            if str(np.array([x, y])) == str(laser_start):
                curr_line.append(f"\033[93m{grid[y][x]}\033[00m")
            elif str(np.array([x, y])) in energized:
                curr_line.append(f"\033[91m{grid[y][x]}\033[00m")
            else:
                curr_line.append(grid[y][x])
        visual.append(curr_line)
    print("\n".join(["".join(l) for l in visual]))

energized = set()
seen_paths = {}
def laser_explore(contraption_grid, l_start, l_next): 
    # visualize(contraption_grid, l_start)
    if not 0 <= l_next[0] < len(contraption_grid[0]) or not 0 <= l_next[1] < len(contraption_grid):
        return
      
    if str(l_start) not in seen_paths:
        seen_paths[str(l_start)] = [str(l_next)]
    elif str(l_next) in seen_paths[str(l_start)]:
        return
    seen_paths[str(l_start)] += [str(l_next)]

    if str(l_next) not in energized:
        energized.add(str(l_next))
    
    next_space = contraption_grid[l_next[1]][l_next[0]]
    direction = l_next-l_start

    is_empty = (next_space == ".")
    is_horizontal_split = (next_space == "-" and direction[1])
    is_vertical_split = (next_space == "|" and direction[0])
    if is_empty and (not is_horizontal_split) and (not is_vertical_split):
        laser_explore(contraption_grid, l_next, l_next+direction)
    elif next_space == "/":
        laser_explore(contraption_grid, l_next, l_next+np.array([-direction[1], -direction[0]]))
    elif next_space == "\\":
        laser_explore(contraption_grid, l_next, l_next+np.array([direction[1], direction[0]]))
    elif next_space == "-":
        laser_explore(contraption_grid, l_next, l_next+np.array([1, 0]))
        laser_explore(contraption_grid, l_next, l_next+np.array([-1, 0]))
    elif next_space == "|":
        laser_explore(contraption_grid, l_next, l_next+np.array([0, 1]))
        laser_explore(contraption_grid, l_next, l_next+np.array([0, -1]))

def generateSolution(filename):
    contraption_grid = parseInputFile(filename)

    laser_start, laser_initial_move = np.array([-1,0]), np.array([0,0])
    laser_explore(contraption_grid, laser_start, laser_initial_move)

    return len(energized)
    
if __name__ == "__main__":
    print(generateSolution("ab.dat"))