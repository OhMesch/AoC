import random
from collections import Counter, deque

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

def pickExploreCut(all_children, runs=20000, branch=3, repeats=3):
    edges = set()
    for k, v in all_children.items():
        for child in v.getChildren():
            edges.add(tuple(sorted([k, child.name])))

    edge_count = Counter(edges)
    for _ in range(runs):
        start = random.choice(list(all_children.values()))
        to_visit = deque([(start, None)])
        seen = set()
        while to_visit:
            current, parent = to_visit.popleft()
            if current not in seen:
                seen.add(current)
                if parent:
                    edge_count[tuple(sorted([parent.name, current.name]))] += 1
                for child in current.getChildren():
                    to_visit.append((child, current))
        if len(seen) < len(all_children):
            print("Not all nodes visited", repeats)
            if repeats == 0:
                printRed((len(seen), len(all_children)-len(seen), len(seen)*(len(all_children)-len(seen))))
    for edge, count in edge_count.most_common(branch):
        u, v = all_children[edge[0]], all_children[edge[1]]
        if repeats > 0:
            print("Removing", u.name, "->", v.name, "(", count, ")", repeats)
            # print(f"Removing {u.name} -> {v.name} ({count}) {repeats}" )
            u.removeChild(v)
            pickExploreCut(all_children, runs, branch, repeats-1)
            u.addChild(v)
    

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

def generateSolution(filename):
    printRed("Generating solution...")
    all_children = parseInputFile(filename)
    pickExploreCut(all_children, 5000, 5)
    
    
if __name__ == "__main__":
    print(generateSolution("ab.dat"))