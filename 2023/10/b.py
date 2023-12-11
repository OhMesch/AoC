from a import getNorth, getSouth, getEast, getWest, getPipeAdjacencies, getStartAdjacencies

inside_point_map = {
    "F": lambda d: {"E": [(1, 1)], "S": [(0, -1), (-1, 0)]}[d],
    '-': lambda d: {"E": [(0, 1)], "W": [(0, -1)]}[d],
    "7": lambda d: {"S": [(-1, 1)], "W": [(0, -1), (1, 0)]}[d],
    '|': lambda d: {"S": [(-1, 0)], "N": [(1, 0)]}[d],
    "L": lambda d: {"N": [(1, -1)], "E": [(-1, 0), (0, 1)]}[d],
    "J": lambda d: {"W": [(-1, -1)], "N": [(0, 1), (1, 0)]}[d],
    "S": lambda d: [], #Can safely ignore Start 
}

#Can safely ignore Start Loc
def getInsidePoints(pipe_map, loc, d):
    x,y = loc
    pipe_type = pipe_map[y][x]

    inside_p = []
    for modification in inside_point_map[pipe_type](d):
        inside_p.append((x + modification[0], y + modification[1]))
    
    return inside_p

def calculateDirection(curr_loc, next_loc):
    if curr_loc[0] == next_loc[0]:
        return "N" if curr_loc[1] > next_loc[1] else "S"
    else:
        return "W" if curr_loc[0] > next_loc[0] else "E"

def chartPipes(pipe_map, start):
    chart = set()
    inside_points = set()

    curr_loc = start 
    next_loc = None
    direction = None
    while next_loc != start:
        chart.add(curr_loc)

        adjs = getPipeAdjacencies(pipe_map, curr_loc) if curr_loc != start else getStartAdjacencies(pipe_map, curr_loc)
        all_next_loc = [x for x in adjs if x not in chart]
        next_loc = all_next_loc[0] if all_next_loc else start

        direction = calculateDirection(curr_loc, next_loc)
        [inside_points.add(p) for p in getInsidePoints(pipe_map, curr_loc, direction)]

        curr_loc = next_loc

    return chart, inside_points

def createGroupMappingsForEmptySpots(simple_map, known_inside):
    seen = set()
    groups = {}
    curr_group = 0
    reverse_inside_flag = False
    for y in range(len(simple_map)):
        for x in range(len(simple_map[y])):
            if (x,y) not in seen and simple_map[y][x] == ".":
                nodes_attached = [(x,y)]
                curr_group_members = set()
                is_inside = False
                while len(nodes_attached) > 0:
                    curr_node = nodes_attached.pop()
                    if curr_node in seen or simple_map[curr_node[1]][curr_node[0]] != ".":
                        continue
                    seen.add(curr_node)
                    curr_group_members.add(curr_node)
                    if curr_node in known_inside:
                        is_inside = True
                        if curr_node[0] == 0 or curr_node[1] == 0:
                            reverse_inside_flag = True
                    if curr_node[0] > 0:
                        nodes_attached.append(getWest(curr_node))
                    if curr_node[0] < len(simple_map[y]) - 1:
                        nodes_attached.append(getEast(curr_node))
                    if curr_node[1] > 0:
                        nodes_attached.append(getNorth(curr_node))
                    if curr_node[1] < len(simple_map) - 1:
                        nodes_attached.append(getSouth(curr_node))

                groups[curr_group] = (curr_group_members, is_inside)
                curr_group += 1

    if reverse_inside_flag:
        for k,v in groups.items():
            groups[k] = (v[0], not v[1])
    return groups

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

    chart, inside_p = chartPipes(pipe_map, start_loc)
    simplified_map = [[x if (i,y_index) in chart else "." for i,x in enumerate(pipe_map[y_index])] for y_index in range(len(pipe_map))]
    unicode_map = ["".join(l).translate(str.maketrans("-|F7LJ", "─│┌┐└┘")) for l in simplified_map]
    
    groups = createGroupMappingsForEmptySpots(simplified_map, inside_p) 
    
    print("\nVISUALIZATION:")
    for y in range(len(unicode_map)):
        curr_line = []
        for x in range(len(unicode_map[y])):
            if unicode_map[y][x] != ".":
                curr_line.append(unicode_map[y][x])
            else:
                for group in groups.values():
                    if (x,y) in group[0] and group[1]:
                        curr_line.append("I")
                        break
                    if (x,y) in group[0] and not group[1]:
                        curr_line.append("O")
                        break
        print("".join(curr_line))
    
    return sum([len(x[0]) for x in groups.values() if x[1]])
    
if __name__ == "__main__":
    print(generateSolution("ab.dat"))