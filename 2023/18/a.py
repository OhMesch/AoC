def parseInputFile(filename):
    with open(filename, "r") as f:
        return([(dirc, int(dist)) for dirc, dist, _ in [l.split() for l in f.readlines()]])

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

def floodFill(starting_point, grid):
        fill = set()
        to_explore = [starting_point]
        while len(to_explore) > 0:
            curr_point = to_explore.pop()
            
            if curr_point in fill:
                continue
            fill.add(curr_point)
            
            x, y = curr_point
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                if 0 <= x + dx < len(grid[0]) and 0 <= y + dy < len(grid):
                    if grid[y+dy][x+dx] == ".":
                        to_explore.append((x+dx, y+dy))
        return fill

direction_map = {
    "U": lambda x, y: (x, y-1),
    "D": lambda x, y: (x, y+1),
    "L": lambda x, y: (x-1, y),
    "R": lambda x, y: (x+1, y),

}
def buildDigGrid(dig_instructions):
    curr_v_dist = 0
    v_dims = [0, 0]
    curr_h_dist = 0
    h_dims = [0, 0]
    for direction, distance in dig_instructions:
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
    for direction, distance in dig_instructions:
        for _ in range(distance):
            curr_x, curr_y = direction_map[direction](curr_x, curr_y)
            dig_grid[curr_y][curr_x] = "#"
    
    flood_points = []
    for y in range(len(dig_grid)):
        flood_points.append((0, y))
        flood_points.append((len(dig_grid[y])-1, y))
    for x in range(len(dig_grid[0])):
        flood_points.append((x, 0))
        flood_points.append((x, (len(dig_grid)-1)))

    outside_points = set()
    for point in flood_points:
        if point not in outside_points and dig_grid[point[1]][point[0]] == '.':
            outside_points = outside_points.union(floodFill(point, dig_grid))

    printColorGrid(dig_grid)

    for y in range(len(dig_grid)):
        for x in range(len(dig_grid[0])):
            if (x, y) not in outside_points and dig_grid[y][x] == '.':
                dig_grid[y][x] = "@"

    printColorGrid(dig_grid)

    return dig_grid

def generateSolution(filename):
    dig_instructions = parseInputFile(filename)
    dig_grid = buildDigGrid(dig_instructions)

    return sum([row.count("#") + row.count("@") for row in dig_grid])
    
if __name__ == "__main__":
    print(generateSolution("ab.dat"))