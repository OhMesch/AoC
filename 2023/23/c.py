from functools import cache

def printGraph(root):
    to_explore = [root]
    seen = set()
    while to_explore:
        curr_node = to_explore.pop()
        if curr_node in seen:
            continue
        seen.add(curr_node)
        print(curr_node)
        for adj in curr_node.getConnections():
            to_explore.append(adj)

def parseInputFile(filename):
    with open(filename, "r") as f:
        return tuple([tuple(line.strip()) for line in f.readlines()])

class Node:
    def __init__(self, name):
        self.name = str(name)
        self.connections = {}

    def addConnection(self, node, weight):
        self.connections[node] = max(self.connections.get(node, 0), weight)
        node.connections[self] = max(node.connections.get(self, 0), weight)

    def getConnections(self):
        return self.connections
    
    def __repr__(self):
        return f"Node {self.name} -> {', '.join([f'{node.name}: {edge}' for node, edge in self.connections.items()])}"

def buildWeightedGraph(grid, start, end):
    root = Node("Start")
    sink = Node("End")
    point_2_node = {start: root, end: sink}
    
    seen = set()
    to_explore = [start]
    while to_explore:
        curr_point = to_explore.pop()
        if curr_point in seen:
            continue
        seen.add(curr_point)

        adj_nodes = findAdjacenciesAndDistance(grid, curr_point)
        if len(adj_nodes) > 2 and curr_point not in point_2_node:
            new_node = Node(curr_point)
            point_2_node[curr_point] = new_node

        for adj in adj_nodes:
            to_explore.append(adj)

    seen = set()
    to_explore = [(start, root, 0)]
    while to_explore:
        curr_point, curr_parent, curr_edge_distance = to_explore.pop()
        
        if point_2_node.get(curr_point, curr_parent) != curr_parent:
            curr_parent.addConnection(point_2_node[curr_point], curr_edge_distance)
            curr_parent = point_2_node[curr_point]
            curr_edge_distance = 0

        if curr_point in seen:
            continue
        seen.add(curr_point)

        for adj in findAdjacenciesAndDistance(grid, curr_point):
            to_explore.append((adj, curr_parent, curr_edge_distance+1))
        
    return root

@cache
def findAdjacenciesAndDistance(grid, position):
    adj = []

    x,y = position
    for dx,dy in [(-1,0), (1,0), (0,-1), (0,1)]:
        if 0<=x+dx<len(grid[0]) and 0<=y+dy<len(grid) and grid[y+dy][x+dx] != "#":
            adj.append((x+dx, y+dy))
    return tuple(adj)

def longestSimplePath(root):
    to_explore = [([root], 0)]
    longest_seen = 0

    while to_explore:
        path, curr_dist = to_explore.pop()
        curr_node = path[-1]
        if curr_node.name == "End":
            longest_seen = max(longest_seen, curr_dist)
            continue
        for adj, edge in [(adj, edge) for adj, edge in curr_node.getConnections().items() if adj not in path]:
            to_explore.append((path+[adj], curr_dist + edge))

    return longest_seen

def generateSolution(filename):
    hike_grid = parseInputFile(filename)
    start = (1, 0)
    end = (len(hike_grid[0])-2, len(hike_grid)-1)

    weighted_graph_root = buildWeightedGraph(hike_grid, start, end)
    return longestSimplePath(weighted_graph_root)
    
if __name__ == "__main__":
    print(generateSolution("ab.dat"))