from a import getNorth, getSouth, getEast, getWest, getPipeAdjacencies, getStartAdjacencies

# def r180(d):
#     return {"N": "S", "E": "W", "S": "N", "W": "E"}[d]

# to_from_direction_conversion = {
#     ("F", "-"): lambda d: {"N": "E", "W": "S"}[d],
#     ("F", "|"): lambda d: {"W": "S", "N": "E"}[d],
#     ("F", "7"): lambda d: {d: r180(d)},
#     ("F", "L"): lambda d: {d: r180(d)},
#     ("F", "J"): lambda d: {d: d},

#     ("7", "-"): lambda d: {"N": "W", "E": "S"}[d],
#     ("7", "|"): lambda d: {"E": "S", "N": "W"}[d],
#     ("7", "L"): lambda d: {d: d},
#     ("7", "J"): lambda d: {d: r180(d)},

#     {"L", "-"}: lambda d: {"S": "E", "W": "N"}[d],
#     {"L", "|"}: lambda d: {"W": "N", "S": "E"}[d],
#     {"L", "J"}: lambda d: {d: r180(d)},

#     {"J", "-"}: lambda d: {"S": "W", "E": "N"}[d],
#     {"J", "|"}: lambda d: {"E": "N", "S": "W"}[d],

#     ("-", "-"): lambda d: {d: d},
#     ("|", "|"): lambda d: {d: d},
# }

# for k,v in to_from_direction_conversion.items():
#     s, e = k
#     if (e, s) not in to_from_direction_conversion:
#         to_from_direction_conversion[(e, s)] = v

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
    # print(f"pipe_type: {pipe_type}, loc: {loc}, d: {d}")
    for modification in inside_point_map[pipe_type](d):
        inside_p.append((x + modification[0], y + modification[1]))
    
    return inside_p

def calcuateDirection(curr_loc, next_loc):
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

        # print(f"curr_loc: {curr_loc}, next_loc: {next_loc}")

        direction = calcuateDirection(curr_loc, next_loc)
        [inside_points.add(p) for p in getInsidePoints(pipe_map, curr_loc, direction)]

        curr_loc = next_loc

    return chart, inside_points

def createGroupMappingsForEmptySpots(simple_map, known_inside):
    seen = set()
    groups = {}
    curr_group = 0
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
    simplied_map = [[x if (i,y_index) in chart else "." for i,x in enumerate(pipe_map[y_index])] for y_index in range(len(pipe_map))]
    simplied_map = ["".join(l).translate(str.maketrans("-|F7LJ", "─│┌┐└┘")) for l in simplied_map]
    
    print("\nVISUAL")
    groups = createGroupMappingsForEmptySpots(simplied_map, inside_p) 

    print(simplied_map)

    for y in range(len(simplied_map)):
        curr_line = []
        for x in range(len(simplied_map[y])):
            if simplied_map[y][x] != ".":
                curr_line.append(simplied_map[y][x])
            else:
                for group in groups.values():
                    if (x,y) in group[0] and group[1]:
                        curr_line.append("I")
                        break
                    if (x,y) in group[0] and not group[1]:
                        curr_line.append("O")
                        break
        print("".join(curr_line))
    print(f"Groups: {[len(v[0]) for v in groups.values() if v[1]]}")
    
    return sum([len(x[0]) for x in groups.values() if not x[1]])
    
if __name__ == "__main__":
    print(generateSolution("ab.dat"))