from heapq import *

def is_same_direction(curr_node, next_node, curr_dir):
    print(f"curr_direction: {curr_dir}, next_node: {next_node}, curr_node: {curr_node}", "is same dir:", (next_node[0] - curr_node[0], next_node[1] - curr_node[1]) == curr_dir)
    if (next_node[0] - curr_node[0], next_node[1] - curr_node[1]) == curr_dir:
        return True
    
def is_opposite_direction(curr_node, next_node, curr_dir):
    if (next_node[0] - curr_node[0], next_node[1] - curr_node[1]) == (-curr_dir[0], -curr_dir[1]):
        return True

def dijkstra_with_limit(grid, direction_limit):
    visited = {}
    to_explore = []
    heappush(to_explore, (0, (0, 0), (1, 1), 0, [(0, 0)]))

    while (len(to_explore)):
        curr_dist, curr_node, curr_direction, curr_count, history = heappop(to_explore)
        print(curr_dist, curr_node, curr_direction, curr_count)
        if curr_node == (len(grid[0])-1, len(grid)-1):
            visual = []
            for y in range(len(grid)):
                curr_line = []
                for x in range(len(grid[0])):
                    if (x, y) in history:
                        curr_line.append(f"\033[93m{grid[y][x]}\033[00m")
                    else:
                        curr_line.append(str(grid[y][x]))
                visual.append(curr_line)
            print("\n".join(["".join(l) for l in visual]))
            return curr_dist
        if curr_count < visited.get((curr_node, curr_direction), 5):
            visited[(curr_node, curr_direction)] = curr_count
        else:
            continue

        if curr_node[0] > 0:
            possible_next = (curr_node[0]-1, curr_node[1])
            possible_direction = (possible_next[0]-curr_node[0], possible_next[1]-curr_node[1])
            if is_same_direction(curr_node, possible_next, curr_direction):
                if curr_count < direction_limit:
                    heappush(to_explore, (curr_dist+grid[possible_next[1]][possible_next[0]], possible_next, curr_direction, curr_count+1, history+[possible_next]))
            elif not is_opposite_direction(curr_node, possible_next, curr_direction):
                heappush(to_explore, (curr_dist+grid[possible_next[1]][possible_next[0]], possible_next, possible_direction, 1, history+[possible_next]))
        
        if curr_node[0] < len(grid[0])-1:
            possible_next = (curr_node[0]+1, curr_node[1])
            possible_direction = (possible_next[0]-curr_node[0], possible_next[1]-curr_node[1])
            if is_same_direction(curr_node, possible_next, curr_direction):
                if curr_count < direction_limit:
                    heappush(to_explore, (curr_dist+grid[possible_next[1]][possible_next[0]], possible_next, curr_direction, curr_count+1, history+[possible_next]))
            elif not is_opposite_direction(curr_node, possible_next, curr_direction):
                heappush(to_explore, (curr_dist+grid[possible_next[1]][possible_next[0]], possible_next, possible_direction, 1, history+[possible_next]))

        if curr_node[1] > 0:
            possible_next = (curr_node[0], curr_node[1]-1)
            possible_direction = (possible_next[0]-curr_node[0], possible_next[1]-curr_node[1])
            if is_same_direction(curr_node, possible_next, curr_direction):
                if curr_count < direction_limit:
                    heappush(to_explore, (curr_dist+grid[possible_next[1]][possible_next[0]], possible_next, curr_direction, curr_count+1, history+[possible_next]))
            elif not is_opposite_direction(curr_node, possible_next, curr_direction):
                heappush(to_explore, (curr_dist+grid[possible_next[1]][possible_next[0]], possible_next, possible_direction, 1, history+[possible_next]))

        if curr_node[1] < len(grid)-1:
            possible_next = (curr_node[0], curr_node[1]+1)
            possible_direction = (possible_next[0]-curr_node[0], possible_next[1]-curr_node[1])
            if is_same_direction(curr_node, possible_next, curr_direction):
                if curr_count < direction_limit:
                    heappush(to_explore, (curr_dist+grid[possible_next[1]][possible_next[0]], possible_next, curr_direction, curr_count+1, history+[possible_next]))
            elif not is_opposite_direction(curr_node, possible_next, curr_direction):
                heappush(to_explore, (curr_dist+grid[possible_next[1]][possible_next[0]], possible_next, possible_direction, 1, history+[possible_next]))

    return None

def parseInputFile(filename):
    with open(filename, "r") as f:
        return([[int(c) for c in l.strip()] for l in f.readlines()])

# def visualize(grid, laser_start):
#     print()
#     visual = []
#     for y in range(len(grid)):
#         curr_line = []
#         for x in range(len(grid[0])):
#             if str(np.array([x, y])) == str(laser_start):
#                 curr_line.append(f"\033[93m{grid[y][x]}\033[00m")
#             elif str(np.array([x, y])) in energized:
#                 curr_line.append(f"\033[91m{grid[y][x]}\033[00m")
#             else:
#                 curr_line.append(grid[y][x])
#         visual.append(curr_line)
#     print("\n".join(["".join(l) for l in visual]))

def generateSolution(filename):
    heat_loss_grid = parseInputFile(filename)

    return dijkstra_with_limit(heat_loss_grid, 3)
    
if __name__ == "__main__":
    print(generateSolution("ab.dat"))