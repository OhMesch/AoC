from a import buildGraph

import re
    
def generateSolution(filename):
    with open(filename) as f:
        lines = [l.strip() for l in f.readlines() if l.strip()]

    instructions = lines[0]
    traverse_graph = buildGraph(lines[1:])
    
    currNodes = [n.split(" = ")[0] for n in lines[1:] if n.split(" = ")[0].endswith("A")]
    instruction_index = 0
    while any([not n.endswith("Z") for n in currNodes]):
        nextNodes = []
        nextInstruction = instructions[instruction_index%len(instructions)]
        if nextInstruction == "L":
            nextNodes.extend([traverse_graph[n][0] for n in currNodes])
        elif nextInstruction == "R":
            nextNodes.extend([traverse_graph[n][1] for n in currNodes])
        currNodes = nextNodes
        instruction_index += 1
    return instruction_index
    
if __name__ == "__main__":
    print(generateSolution("ab.dat"))