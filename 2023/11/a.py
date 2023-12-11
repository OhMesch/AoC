import numpy as np
from queue import PriorityQueue 

def xy2i(x,y,grid):
    return y*len(grid[0]) + x

def i2xy(i,grid):
    return (i%len(grid[0]), i//len(grid[0]))

def generateBaseAdjacencyMatrix(grid, ex_row, ex_col):
    adj = np.zeros((len(grid)*len(grid[0]), len(grid)*len(grid[0])))+float("inf")
    for y in range(len(grid)):
        for x in range(0,len(grid[0])):
            node = xy2i(x,y,grid)
            adj[node, node] = 0
            if x > 0:
                adj[node, xy2i(x-1,y,grid)] = 1 + int(x-1 in ex_col)
            if x < len(grid[0])-1:
                adj[node, xy2i(x+1,y,grid)] = 1 + int(x+1 in ex_col)
            if y > 0:
                adj[node, xy2i(x,y-1,grid)] = 1 + int(y-1 in ex_row)
            if y < len(grid)-1:
                adj[node, xy2i(x,y+1,grid)] = 1 + int(y+1 in ex_row)
    return adj

def dijkstra_till_find_all_goals(adj, start, goals):
    visited = set()
    to_explore = PriorityQueue()
    to_explore.put((0, start))

    while any([adj[start, end] == float("inf") for end in goals]) and not to_explore.empty():
        curr_dist, curr_node = to_explore.get()
        
        if curr_node in visited:
            continue

        visited.add(curr_node)

        adj[start, curr_node] = curr_dist
        adj[curr_node, start] = curr_dist

        for next_node, dist in [(node, dist) for node, dist in enumerate(adj[curr_node]) if dist != float('inf') and node not in visited]:
            to_explore.put((curr_dist + dist, next_node))

    return adj


def generateSolution(filename):
    with open(filename, "r") as f:
        space_grid = np.array([list(l.strip()) for l in f.readlines()], dtype=str)

    expanded_rows = [i for i,r in enumerate(space_grid) if "#" not in r]
    expanded_cols = [i for i,c in enumerate(np.transpose(space_grid)) if "#" not in c]

    adj_matrix = generateBaseAdjacencyMatrix(space_grid, expanded_rows, expanded_cols)
    
    galaxies_i = np.where(space_grid == "#")
    galaxies = [xy2i(x,y,space_grid) for x,y in zip(galaxies_i[1], galaxies_i[0])]


    print("START")
    count = 0
    for g in galaxies:
        count += 1
        adj_matrix = dijkstra_till_find_all_goals(adj_matrix, g, galaxies)
        galaxy_shortest_paths = adj_matrix[galaxies,:][:,galaxies]
        # print("\n", count)
        # print(galaxy_shortest_paths)

        if float("inf") not in galaxy_shortest_paths:
            return int(np.sum(np.triu(galaxy_shortest_paths)))
    
if __name__ == "__main__":
    print(generateSolution("ab.dat"))