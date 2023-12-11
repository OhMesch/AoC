def getNorth(loc):
    return (loc[0], loc[1] - 1)

def getSouth(loc):
    return (loc[0], loc[1] + 1)

def getEast(loc):
    return (loc[0] + 1, loc[1])

def getWest(loc):
    return (loc[0] - 1, loc[1])

def getStartAdjacencies(pipe_map, loc):
    adj = []

    #! My start is not on the edge, not checking index errors
    for neighbor in [getNorth(loc), getSouth(loc), getEast(loc), getWest(loc)]:
        neighbor_adjs = getPipeAdjacencies(pipe_map, neighbor)
        if loc in neighbor_adjs:
            adj.append(neighbor)

    assert len(adj) == 2
    return adj

def getPipeAdjacencies(pipe_map, loc):
    pipe_type = pipe_map[loc[1]][loc[0]]

    adjs = []
    if pipe_type == "|":
        adjs = [getNorth(loc), getSouth(loc)]
    elif pipe_type == "-":
        adjs = [getWest(loc),getEast(loc)]
    elif pipe_type == "L":
        adjs = [getNorth(loc),getEast(loc)]
    elif pipe_type == "J":
        adjs = [getNorth(loc), getWest(loc)]
    elif pipe_type == "7":
        adjs = [getSouth(loc), getWest(loc)]
    elif pipe_type == "F":
        adjs = [getSouth(loc),getEast(loc)]

    return adjs

def chartPipes(pipe_map, start):
    chart = {}

    depth = 1
    curr_locs = [start]
    while len(curr_locs) > 0:
        next_locs = []
        for loc in curr_locs:
            adjs = getPipeAdjacencies(pipe_map, loc) if depth > 1 else getStartAdjacencies(pipe_map, loc)
            for adj in adjs:
                if adj not in chart:
                    chart[adj] = depth 
                    next_locs.append(adj)
        depth += 1
        curr_locs = next_locs

    return chart

def generateSolution(filename):
    pipe_map = []
    with open(filename) as f:
        for line in f.readlines():
            pipe_map.append(line.strip())    

    start_loc = None
    for y_start in range(len(pipe_map)):
        for x_start in range(len(pipe_map[y_start])):
            if pipe_map[y_start][x_start] == "S":
                start_loc = (x_start, y_start)
                break

    chart = chartPipes(pipe_map, start_loc)

    return max(chart.values())
    
if __name__ == "__main__":
    print(generateSolution("ab.dat"))