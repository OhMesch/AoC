import re

def buildGraph(mappings):
    graph = {}
    for m in mappings:
        parent, left, right = re.search(r"(\w+) = \((\w+), (\w+)\)", m).groups()
        graph[parent] = (left, right)
    return graph
    
def generateSolution(filename):
    with open(filename) as f:
        lines = [l.strip() for l in f.readlines() if l.strip()]

    instructions = lines[0]
    traverse_graph = buildGraph(lines[1:])
    
    currNode = "AAA"
    instruction_index = 0
    while currNode != "ZZZ":
        nextInstruction = instructions[instruction_index%len(instructions)]
        # print(currNode, instruction_index, nextInstruction)
        # print(traverse_graph[currNode])
        if nextInstruction == "L":
            currNode = traverse_graph[currNode][0]
        elif nextInstruction == "R":
            currNode = traverse_graph[currNode][1]
        instruction_index += 1
    return instruction_index
    
if __name__ == "__main__":
    print(generateSolution("ab.dat"))