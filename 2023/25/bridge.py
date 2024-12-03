from collections import Counter
from itertools import permutations
import random

class Node:
    def __init__(self, name):
        self.name = name
        self.children = set()
    
    def addChild(self, child):
        self.children.add(child)
        child.children.add(self)

    def removeChild(self, child):
        self.children.remove(child)
        child.children.remove(self)
    
    def getChildren(self):
        return self.children
    
    # def __str__(self):
    #     return f"Node: {self.name} -> {[c.name for c in self.children]}"

def parseInputFile(filename):
    all_nodes = {}
    with open(filename, "r") as f:
        for line in f.readlines():
            parent, children = line.strip().split(":")
            if parent not in all_nodes:
                all_nodes[parent] = Node(parent)
            for child in children.strip().split(" "):
                if child not in all_nodes:
                    all_nodes[child] = Node(child)
                all_nodes[parent].addChild(all_nodes[child])
    return all_nodes

def printRed(text):
    print("\033[91m{}\033[00m".format(text))

def getArticulationPoints(i, d, edges):
    a_visited = set()
    a_depth = {}
    a_low = {}
    a_point = []

    def getArticulationPointsHelper(i, d, parent):
        a_visited.add(i)
        a_depth[i] = d
        a_low[i] = d

        for child in i.getChildren():
            if child not in a_visited:
                getArticulationPointsHelper(child, d+1, i)
                if a_depth[i] < a_low[child]:
                    a_point.append((i.name, child.name))
                    a_low[i] = min(a_low[i], a_low[child])
            else:
                if child != parent:
                    a_low[i] = min(a_low[i], a_depth[child])
        
    getArticulationPointsHelper(i, d, None)
    if len(a_point) == 3:
        print()
        printRed("Articulation points for edges {}:".format(edges))
        for u,v in a_point:
            printRed((u, v))

def generateSolution(filename):
    printRed("Generating solution...")
    all_children = parseInputFile(filename)
    
    edges = set()
    for k, v in all_children.items():
        for child in v.getChildren():
            edges.add(tuple(sorted([k, child.name])))

    all_edges = list(edges)
    first_node = all_children[list(all_children.keys())[0]]
    for i,edge_perm in enumerate(permutations(all_edges, 2)):
        # print(edge_perm)
        if i%10000 == 0:
            all_perm = len(all_edges)*(len(all_edges)-1)
            print("Round {} of {}.".format(i, all_perm))
        for edge in edge_perm:
            all_children[edge[0]].removeChild(all_children[edge[1]])

        first_node = all_children[random.choice(list(all_children.keys()))]

        getArticulationPoints(first_node, 0, edge_perm)
            
        for edge in edge_perm:
            all_children[edge[0]].addChild(all_children[edge[1]])

if __name__ == "__main__":
    print(generateSolution("ab.dat"))