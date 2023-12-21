from functools import cache

def parseInputFile(filename):
    start_pos = None
    garden_grid = []
    with open(filename) as f:
        for line in f:
            garden_grid.append(list(line.strip()))
    for y in range(len(garden_grid)):
        for x in range(len(garden_grid[y])):
            if garden_grid[y][x] == 'S':
                start_pos = (x, y)
                garden_grid[y][x] = '.'
                return start_pos, tuple([tuple(row) for row in garden_grid])

@cache
def exploreAdjacent(origin, garden_grid):
    adjacent = set()

    for delta in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        x, y = origin
        x += delta[0]
        y += delta[1]
        if x >= 0 and x < len(garden_grid[y]) and y >= 0 and y < len(garden_grid) and garden_grid[y][x] == '.':
            adjacent.add((x, y))

    return adjacent

def exploreGarden(start, garden_grid, steps):
    can_reach_by_step = [{start}, exploreAdjacent(start, garden_grid)]

    for step in range(2, steps+1):
        curr_can_reach = can_reach_by_step[step-2]
        for prior_pos in can_reach_by_step[step-1]:
            curr_can_reach = curr_can_reach.union(exploreAdjacent(prior_pos, garden_grid))
        
        can_reach_by_step.append(curr_can_reach)

    return can_reach_by_step

def generateSolution(filename, steps = 64):
    start, garden_grid = parseInputFile(filename)
    exploration = exploreGarden(start, garden_grid, steps)
    print(exploreAdjacent.cache_info())
    return len(exploration[steps])
    
if __name__ == "__main__":
    print(generateSolution("ab.dat"))