from heapq import *
import numpy as np

def dijkstra_with_limits(grid, min_move, max_move):
    visited = set()
    to_explore = []

    start = (0, 0)
    end = (len(grid[0])-1, len(grid)-1)
    heappush(to_explore, (0, start, []))

    while (len(to_explore)):
        curr_dist, curr_node, history = heappop(to_explore)

        # if len(history) < 6 and curr_node[0] ==6:
        # print(f"@curr_node: {curr_node} w/ curr_dist: {curr_dist} via {history}")
        if curr_node == end:
            visual = []
            for y in range(len(grid)):
                curr_line = []
                for x in range(len(grid[0])):
                    if (x, y) == curr_node:
                        curr_line.append(f"\033[93m{grid[y][x]}\033[00m")
                    elif (x, y) in history:
                        curr_line.append(f"\033[91m{grid[y][x]}\033[00m")
                    else:
                        curr_line.append(str(grid[y][x]))
                visual.append(curr_line)
            print("\n".join(["".join(l) for l in visual]))
            # print("FOUND: ", curr_dist)
            return curr_dist
        
        if history:
            last_move = np.array(curr_node) - np.array(history[-1])
        else:
            last_move = np.array([0, 0])

        node_and_heading = (curr_node, tuple(last_move/max(abs(last_move))))
        if node_and_heading in visited:
            continue
        else:
            visited.add(node_and_heading)

        if last_move[0] == 0:
            for travel_dist in range(min_move, min(curr_node[0], max_move)+1):
                current_slice = grid[curr_node[1], curr_node[0]-travel_dist:curr_node[0]]
                heappush(to_explore, (curr_dist+sum(current_slice), (curr_node[0]-travel_dist, curr_node[1]), history+[curr_node]))
            
            for travel_dist in range(min_move, min(len(grid[0])-curr_node[0]-1, max_move)+1):
                current_slice = grid[curr_node[1], curr_node[0]+1:curr_node[0]+travel_dist+1]
                heappush(to_explore, (curr_dist+sum(current_slice), (curr_node[0]+travel_dist, curr_node[1]), history+[curr_node]))

        if last_move[1] == 0:
            for travel_dist in range(min_move, min(curr_node[1], max_move)+1):
                current_slice = grid[curr_node[1]-travel_dist:curr_node[1], curr_node[0]]
                heappush(to_explore, (curr_dist+sum(current_slice), (curr_node[0], curr_node[1]-travel_dist), history+[curr_node]))
            
            for travel_dist in range(min_move, min(len(grid)-curr_node[1]-1, max_move)+1):
                current_slice = grid[curr_node[1]+1:curr_node[1]+travel_dist+1, curr_node[0]]
                heappush(to_explore, (curr_dist+sum(current_slice), (curr_node[0], curr_node[1]+travel_dist), history+[curr_node]))

    return None

def parseInputFile(filename):
    with open(filename, "r") as f:
        return(np.array([[int(c) for c in l.strip()] for l in f.readlines()]))

def generateSolution(filename, limits=(4,10)):
    heat_loss_grid = parseInputFile(filename)

    return dijkstra_with_limits(heat_loss_grid, limits[0], limits[1])
    
if __name__ == "__main__":
    print(generateSolution("ab.dat", (4,10)))