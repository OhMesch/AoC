from collections import deque
from functools import cache

def parseInputFile(filename):
    with open(filename, "r") as f:
        return tuple([tuple(line.strip()) for line in f.readlines()])

@cache
def findAdjacenciesAndDistance(grid, position):
    adj = []

    x,y = position
    for dx,dy in [(-1,0), (1,0), (0,-1), (0,1)]:
        if 0<=x+dx<len(grid) and 0<=y+dy<len(grid[0]) and grid[y+dy][x+dx] != "#":
            adj.append((x+dx, y+dy))
    return tuple(adj)


def findLongestPath(hike_grid, start, end):
    to_explore = deque([[start]])
    longest_seen = 0

    while len(to_explore):
        curr_history = to_explore.popleft()
        curr_point = curr_history[-1]
        if curr_point == end:
            longest_seen = max(longest_seen, len(curr_history)-1)
            continue

        for adj in findAdjacenciesAndDistance(hike_grid, curr_point):
            if adj not in curr_history:
                to_explore.append((curr_history + [adj]))

    print(findAdjacenciesAndDistance.cache_info())
    return longest_seen

def generateSolution(filename):
    hike_grid = parseInputFile(filename)
    start = (1, 0)
    end = (len(hike_grid[0])-2, len(hike_grid)-1)
    return findLongestPath(hike_grid, start, end)
    
if __name__ == "__main__":
    print(generateSolution("ab.dat"))