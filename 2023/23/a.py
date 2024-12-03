from collections import deque
from functools import cache

def parseInputFile(filename):
    with open(filename, "r") as f:
        return tuple([tuple(line.strip()) for line in f.readlines()])

slides = {
    ".": lambda x,y: ((x, y), 1),
    ">": lambda x,y: ((x+1, y), 2),
    "v": lambda x,y: ((x, y+1), 2),
    "<": lambda x,y: ((x-1, y), 2),
    "^": lambda x,y: ((x, y+1), 2),
}

@cache
def findAdjacenciesAndDistance(grid, position):
    adj = []

    x,y = position
    for dx,dy in [(-1,0), (1,0), (0,-1), (0,1)]:
        if 0<=x+dx<len(grid[0]) and 0<=y+dy<len(grid) and grid[y+dy][x+dx] in slides:
            adj.append(slides[grid[y+dy][x+dx]](x+dx, y+dy))
    return tuple(adj)


def findLongestPath(hike_grid, start, end):
    to_explore = deque([([start], 0)])
    longest_seen = 0

    while len(to_explore):
        curr_history, curr_dist = to_explore.popleft()
        curr_point = curr_history[-1]
        if curr_point == end:
            longest_seen = max(longest_seen, curr_dist)
            continue

        for adj, dist in findAdjacenciesAndDistance(hike_grid, curr_point):
            if adj not in curr_history:
                to_explore.append((curr_history + [adj], curr_dist + dist))

    print(findAdjacenciesAndDistance.cache_info())
    return longest_seen

def generateSolution(filename):
    hike_grid = parseInputFile(filename)
    start = (1, 0)
    end = (len(hike_grid[0])-2, len(hike_grid)-1)
    return findLongestPath(hike_grid, start, end)
    
if __name__ == "__main__":
    print(generateSolution("ab.dat"))