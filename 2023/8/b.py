from a import buildGraph

from math import lcm
    
def generateSolution(filename):
    with open(filename) as f:
        lines = [l.strip() for l in f.readlines() if l.strip()]

    instructions = lines[0]
    traverse_graph = buildGraph(lines[1:])
    
    start_nodes = [n.split(" = ")[0] for n in lines[1:] if n.split(" = ")[0].endswith("A")]
    end_nodes = [n.split(" = ")[0] for n in lines[1:] if n.split(" = ")[0].endswith("Z")]
    
    distances_to_end = {}
    for s in start_nodes:
        curr_node = s
        search_index = 0
        seen_nodes_for_instruction = set()
        while True:
            nextInstruction = instructions[search_index%len(instructions)]
            curr_node = traverse_graph[curr_node][0] if nextInstruction == "L" else traverse_graph[curr_node][1]
            search_index += 1

            if curr_node in end_nodes:
                distances_to_end.setdefault(s, []).append((curr_node, search_index, search_index % len(instructions)))

            if (curr_node, search_index % len(instructions)) in seen_nodes_for_instruction:
                break
            seen_nodes_for_instruction.add((curr_node, search_index % len(instructions)))
    
    # print(distances_to_end)
    # Examining our distances to end, all starts go to distinctive ends before looping, nice!
    # Also loops do always complete a full cycles
    lcd_factors = [v[0][1] for v in distances_to_end.values()] #Solution is specifically molded to assumptions listed above because they just happen to be true for this input data
    print(lcd_factors)
    return lcm(*lcd_factors)
    
if __name__ == "__main__":
    print(generateSolution("ab.dat"))