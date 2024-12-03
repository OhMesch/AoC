import re
import math

def parseInputFile(filename):
    workflows = {}
    with open(filename, "r") as f:
        while currline := f.readline().strip():
            workflow_name = re.match(r"(\w+){", currline).group(1)
            workflow_details = re.search(r"{(.+)}", currline).group(1).split(",")
            workflows[workflow_name] = workflow_details
    workflows['A'] = ['A']
    workflows['R'] = ['R']
    return workflows

def exploreWorkflow(workflows, workflow_name, rule, ranges, history = []):
    current_rule = workflows[workflow_name][rule]
    if ":" not in current_rule:
        goto = current_rule
        if goto == 'A':
            print(f"Found a solution:\n{ranges}\n{history}\n")
            return [ranges]
        if goto == 'R':
            return []
        return exploreWorkflow(workflows, goto, 0, ranges, history+[workflow_name])
    else:
        condition, goto = current_rule.split(":")
        range_to_modify = condition[0]
        operator = condition[1]
        value = int(condition[2:])

        take_ranges = []
        ignore_ranges = []
        # if value == 2662: print(ranges)
        if operator == '<':
            if ranges[range_to_modify][0] < value:
                print()
                print("in take <")
                print(ranges)
                print(current_rule)
                new_ranges = ranges.copy()
                new_ranges[range_to_modify] = (ranges[range_to_modify][0], min(ranges[range_to_modify][1], value))
                take_ranges =  exploreWorkflow(workflows, goto, 0, new_ranges, history+[workflow_name])
            if ranges[range_to_modify][1] > value:
                # print()
                # print("in ignore <")
                # print(ranges)
                # print(current_rule)
                # if value == 2662: print("in ignore <")
                new_ranges = ranges.copy()
                new_ranges[range_to_modify] = (max(ranges[range_to_modify][0], value), ranges[range_to_modify][1])
                ignore_ranges = exploreWorkflow(workflows, workflow_name, rule+1, new_ranges, history+[workflow_name])
            return take_ranges + ignore_ranges
        else:
            if ranges[range_to_modify][1] > value:
                # print()
                # print("in take >")
                # print(ranges)
                # print(current_rule)
                new_ranges = ranges.copy()
                new_ranges[range_to_modify] = (max(ranges[range_to_modify][0], value+1), ranges[range_to_modify][1])
                take_ranges = exploreWorkflow(workflows, goto, 0, new_ranges, history+[workflow_name])
            if ranges[range_to_modify][0] < value:
                print()
                print("in ignore <")
                print(ranges)
                print(current_rule)
                new_ranges = ranges.copy()
                new_ranges[range_to_modify] = (ranges[range_to_modify][0], min(ranges[range_to_modify][1], value+1))
                ignore_ranges = exploreWorkflow(workflows, workflow_name, rule+1, new_ranges, history+[workflow_name])
            return take_ranges + ignore_ranges


def generateSolution(filename):
    workflows = parseInputFile(filename)
    possible_ranges = exploreWorkflow(workflows, 'in', 0, {'x': (1, 4001), 'm': (1, 4001), 'a': (1, 4001), 's': (1, 4001)})
    running_sum = 0
    running_sum_extra = 0
    for p in possible_ranges:
        # print(p)
        print(p, " => ", math.prod([r[1]-r[0] for r in p.values()]))
        running_sum += math.prod([r[1]-r[0] for r in p.values()])
        running_sum_extra += math.prod([r[1]-r[0]+1 for r in p.values()])
    print(running_sum, running_sum_extra)
    seen_sets = set()
    for p in possible_ranges:
        for p2 in possible_ranges:
            if p == p2: continue
            if all([sum(range(max(p['x'][0], p2['x'][0]), min(p['x'][1], p2['x'][1])+1)), sum(range(max(p['m'][0], p2['m'][0]), min(p['m'][1], p2['m'][1])+1)), sum(range(max(p['a'][0], p2['a'][0]), min(p['a'][1], p2['a'][1])+1)), sum(range(max(p['s'][0], p2['s'][0]), min(p['s'][1], p2['s'][1])+1))]):
                print()
                print("Overlap")
                print((range(max(p['x'][0], p2['x'][0]), min(p['x'][1], p2['x'][1])+1)))
                print((range(max(p['m'][0], p2['m'][0]), min(p['m'][1], p2['m'][1])+1)))
                print((range(max(p['a'][0], p2['a'][0]), min(p['a'][1], p2['a'][1])+1)))
                print((range(max(p['s'][0], p2['s'][0]), min(p['s'][1], p2['s'][1])+1)))
    return running_sum
    
if __name__ == "__main__":
    print(generateSolution("ab.dat"))