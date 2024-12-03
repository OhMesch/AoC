import re

def parseInputFile(filename):
    workflows = {}
    parts = []
    with open(filename, "r") as f:
        while currline := f.readline().strip():
            workflow_name = re.match(r"(\w+){", currline).group(1)
            workflow_details = re.search(r"{(.+)}", currline).group(1).split(",")
            workflows[workflow_name] = workflow_details
        while currline := f.readline().strip():
            x,m,a,s = re.findall(r"\d+", currline)
            parts.append({'x': int(x), 'm': int(m), 'a': int(a), 's': int(s)})
    return workflows, parts

def processParts(parts, workflows):
    accepted_parts = []
    for part in parts:
        step_idx = 0
        current_steps = workflows['in']
        while step_idx < len(current_steps):
            if ":" not in current_steps[step_idx]:
                goto = current_steps[step_idx]
                if goto == 'A':
                    accepted_parts.append(part)
                    break
                if goto == 'R':
                    break
                current_steps = workflows[goto]
                step_idx = 0
            else:
                condition, goto = current_steps[step_idx].split(":")
                if eval(f"{part[condition[0]]}{condition[1:]}"):
                    if goto == 'A':
                        accepted_parts.append(part)
                        break
                    if goto == 'R':
                        break
                    current_steps = workflows[goto]
                    step_idx = 0
                else:
                    step_idx += 1

    return accepted_parts

def generateSolution(filename):
    workflows, parts = parseInputFile(filename)
    accepted_parts = processParts(parts, workflows)

    running_sum = 0
    for part in accepted_parts:
        running_sum += part['x'] + part['m'] + part['a'] + part['s']
    return running_sum
    
if __name__ == "__main__":
    print(generateSolution("ab.dat"))