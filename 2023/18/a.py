import re
import numpy as np

def parseInputFile(filename):
    with open(filename, "r") as f:
        # return([[(d, int(dist), color) for d, dist, color in l.split()] for l in f.readlines()])
        return([(dirc, int(dist), c) for dirc, dist, c in [l.split() for l in f.readlines()]])

    
def printGrid(grid):
    print()
    for row in grid:
        print("".join(row))

def printColorGrid(grid):
    print()
    for row in grid:
        curr_row = []
        for c in row:
            if c == "#":
                curr_row.append("\033[4m" + c + "\033[0m")
            elif c == "/":
                curr_row.append("\033[92m" + c + "\033[0m")
            elif c == "@":
                curr_row.append("\033[91m" + c + "\033[0m")
            else:
                curr_row.append(c)
        print("".join(curr_row))

direction_map = {
    "U": lambda x, y: (x, y-1),
    "D": lambda x, y: (x, y+1),
    "L": lambda x, y: (x-1, y),
    "R": lambda x, y: (x+1, y),

}
def buildDigGrid(dig_instructions):
    print(dig_instructions)

    curr_v_dist = 0
    v_dims = [0, 0]
    curr_h_dist = 0
    h_dims = [0, 0]
    for direction, distance, _ in dig_instructions:
        if direction == "U":
            curr_v_dist -= distance
            v_dims[0] = min(v_dims[0], curr_v_dist)
        elif direction == "D":
            curr_v_dist += distance
            v_dims[1] = max(v_dims[1], curr_v_dist)
        elif direction == "L":
            curr_h_dist -= distance
            h_dims[0] = min(h_dims[0], curr_h_dist)
        elif direction == "R":
            curr_h_dist += distance
            h_dims[1] = max(h_dims[1], curr_h_dist)

    dig_grid = [['.' for _ in range(h_dims[1] - h_dims[0] + 1)] for _ in range(v_dims[1] - v_dims[0] + 1)]
    
    curr_x, curr_y = (0, 0)
    curr_x, curr_y = (-h_dims[0], -v_dims[0])
    dig_grid[curr_y][curr_x] = "#"
    for direction, distance, _ in dig_instructions:
        for _ in range(distance):
            curr_x, curr_y = direction_map[direction](curr_x, curr_y)
            print(f"({curr_x}, {curr_y}) -> {direction, distance} -> {len(dig_grid[0]), len(dig_grid)} w/ ranges (x, y): {h_dims, v_dims}")
            dig_grid[curr_y][curr_x] = "#"

    #loop over all points in grid where x or y is 0
    
    outside_points = set()
    def floodFill(starting_point, grid):
        fill = set(starting_point)
        

    for y in range(len(dig_grid)):
        if dig_grid[y][0] == ".":
            outside_points.union(floodFill((0, y), dig_grid))
        if dig_grid[y][-1] == ".":
            outside_points.union(floodFill((0, y), dig_grid))
    for x in range(len(dig_grid[0])):
        if dig_grid[0][x] == ".":
            outside_points.union(floodFill((x, 0), dig_grid))
        if dig_grid[-1][x] == ".":
            outside_points.union(floodFill((x, 0), dig_grid))
        
        

    # # dig_grid = np.rot90(dig_grid)

    # printGrid(dig_grid)
    # dig_grid = ["".join(row) for row in dig_grid]

    # print()
    # rx = re.compile(r"(?<=#)[.]+(?=#)")
    # # match_count = 0
    # # def replaceEveryOther(match):
    # #     nonlocal match_count
    # #     match_count += 1
    # #     if match_count % 2 == 1:
    # #         return r'@'*len(match.group())
    # #     else:
    # #         return match.group()
    
    # for y in range(len(dig_grid)):
    #     # match_count = 0
    #     dig_grid[y] = rx.sub(lambda x: r'/'*len(x.group()), dig_grid[y])

    # printColorGrid(dig_grid)

    # dig_grid = np.rot90([list(row) for row in dig_grid])
    # dig_grid = ["".join(row) for row in dig_grid]

    # rx = re.compile(r"(?<=#)[/]+(?=#)")
    # for y in range(len(dig_grid)):
    #     dig_grid[y] = rx.sub(lambda x: r'@'*len(x.group()), dig_grid[y])
    
    # dig_grid = np.rot90([list(row) for row in dig_grid], k=-1)
    # dig_grid = ["".join(row) for row in dig_grid]
    
    # printColorGrid(dig_grid)

    return dig_grid

def generateSolution(filename):
    dig_instructions = parseInputFile(filename)
    dig_grid = buildDigGrid(dig_instructions)

    return sum([row.count("#") + row.count("@") for row in dig_grid])
    
if __name__ == "__main__":
    print(generateSolution("ab.dat"))